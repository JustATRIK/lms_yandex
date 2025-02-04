import json
import os
from pathlib import Path

import dotenv
import requests
from bs4 import BeautifulSoup

TARGET_LESSONS = [13025]
BASE_PATH = Path("./")
GROUP_ID = 5141

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


def get_solution_url(solution_id, user_id):
    return SOLUTION_URL.replace("$solution_id", str(solution_id)).replace("$user_id", str(user_id))


dotenv.load_dotenv()
session = requests.Session()
session.cookies.set('tmr_lvid', os.getenv("tmr_lvid"))
session.cookies.set('_gcl_au', os.getenv("_gcl_au"))
session.cookies.set('tmr_lvidTS', os.getenv("tmr_lvidTS"))
session.cookies.set('sessionid', os.getenv("sessionid"))
user_id = os.getenv("user_id")

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

        code = ""
        for solution in problem_solutions_json["submissions"]:
            if solution["status"] == "correct":
                code = solution["reply"]["code"]
        if code == "":
            continue

        problem_name = str(id_s)

        solution_save_path = (BASE_PATH / format_path_dir(contest_name) / f"{id_s}.{SAVE_EXT}")
        solution_save_path.parent.mkdir(exist_ok=True, parents=True)
        if solution_save_path.exists():
            os.remove(solution_save_path)

        with open(solution_save_path, "a", encoding="utf-8") as file:
            file.write(code)
            file.flush()
        print(f"Saved ({id_s}/{len(problems)}):", solution_save_path)

