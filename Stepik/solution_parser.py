import json
import os
from pathlib import Path

import dotenv
import requests
from bs4 import BeautifulSoup

TARGET_COURSE = 111246
TARGET_LESSONS = [663332]
BASE_PATH = Path("./")
GROUP_ID = 5141

SECTION_URL = f"https://stepik.org/api/sections/"
UNIT_URL = f"https://stepik.org/api/units/?ids%5B%5D="
COURSE_URL = f"https://stepik.org/api/courses/"
ATTEMPT_URL = f"https://stepik.org/api/attempts?step=$solution_id&user=$user_id"
SOLUTION_URL = f"https://stepik.org/api/submissions?order=desc&step=$solution_id&user=$user_id"
LESSON_URL = f"https://stepik.org/api/lessons?ids%5B%5D=$lesson_id"
SAVE_EXT = "cpp"


def validate_response(response, exit_on_fail=False):
    if response.status_code != 200:
        print("Error! Status code", response.status_code)
        print(response.text)
        if exit_on_fail:
            exit()
        return False
    return True


def format_path_dir(path_dir):
    return path_dir.replace(".", "").replace(":", "").replace("?", "").replace("!", "").replace(",", "").replace("/", "").replace("\\", "")


def get_lesson_url(lesson_id):
    return LESSON_URL.replace("$lesson_id", str(lesson_id))


def get_section_url(section):
    return SECTION_URL + str(section)


def get_course_url(course):
    return COURSE_URL + str(course)


def get_solution_url(solution_id, user_id):
    return SOLUTION_URL.replace("$solution_id", str(solution_id)).replace("$user_id", str(user_id))


def get_attempt_url(solution_id, user_id):
    return ATTEMPT_URL.replace("$solution_id", str(solution_id)).replace("$user_id", str(user_id))


dotenv.load_dotenv()
session = requests.Session()
session.cookies.set('tmr_lvid', os.getenv("tmr_lvid"))
session.cookies.set('_gcl_au', os.getenv("_gcl_au"))
session.cookies.set('tmr_lvidTS', os.getenv("tmr_lvidTS"))
session.cookies.set('sessionid', os.getenv("sessionid"))
user_id = os.getenv("user_id")

if TARGET_COURSE is not None:
    TARGET_LESSONS.clear()
    response = session.get(get_course_url(TARGET_COURSE))
    validate_response(response, exit_on_fail=True)

    for section in json.loads(response.text)["courses"][0]["sections"]:
        print(f"Processing {section} section")
        section_response = session.get(get_section_url(section))
        if not validate_response(section_response, exit_on_fail=False):
            print("Skipping course")
            continue

        units_url = UNIT_URL + "&ids%5B%5D=".join(map(str, json.loads(section_response.text)["sections"][0]["units"]))
        units_response = session.get(units_url)
        if not validate_response(units_response, exit_on_fail=False):
            print("Skipping course")

        for unit in json.loads(units_response.text)["units"]:
            TARGET_LESSONS.append(unit["lesson"])

    print(f"Found {len(TARGET_LESSONS)} lessons in course")

for lesson_id in TARGET_LESSONS:
    response = session.get(get_lesson_url(lesson_id))
    if not validate_response(response, exit_on_fail=False):
        continue
    print(response.text)
    response = json.loads(response.text)

    if len(response["lessons"]) == 0:
        continue

    problems = response["lessons"][0]["steps"]
    contest_name = response["lessons"][0]["title"]
    print(f"Found {len(problems)} problems in lesson {contest_name}")

    id_s = 0
    for problem_id in problems:
        id_s += 1
        problem_solutions = session.get(get_solution_url(problem_id, user_id))
        if not validate_response(problem_solutions, exit_on_fail=False):
            continue

        problem_solutions_json = json.loads(problem_solutions.text)
        if len(problem_solutions_json["submissions"]) < 1:
            continue

        problem_solution = None
        attempt_id = -1
        for solution in problem_solutions_json["submissions"]:
            if solution["status"] == "correct":
                attempt_id = solution["attempt"]
                problem_solution = {"reply": solution["reply"]}
                break
        if problem_solution is None:
            continue

        problem_attempts = session.get(get_attempt_url(problem_id, user_id))
        if not validate_response(problem_attempts, exit_on_fail=False):
            continue

        dataset = ""
        for attempt in json.loads(problem_attempts.text)["attempts"]:
            if attempt["id"] == attempt_id:
                dataset = attempt["dataset"]

        if dataset != "" and isinstance(dataset, dict) and "options" in dataset:
            problem_solution["dataset"] = dataset["options"]
            print(f"Using dataset {dataset['options']}")

        problem_name = str(id_s)

        solution_save_path = (BASE_PATH / "plain" / f"{problem_id}.json")
        solution_save_path.parent.mkdir(exist_ok=True, parents=True)
        if solution_save_path.exists():
            os.remove(solution_save_path)

        with open(solution_save_path, "w", encoding="utf-8") as file:
            json.dump(problem_solution, file)
            file.flush()
        print(f"Saved ({id_s}/{len(problems)}):", solution_save_path)

