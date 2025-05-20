import json
import os
from pathlib import Path

import dotenv
import requests

TARGET_COURSE = 111246
TARGET_LESSONS = [663330]
BASE_PATH = Path("./")
GROUP_ID = 5141

SECTION_URL = f"https://stepik.org/api/sections/"
UNIT_URL = f"https://stepik.org/api/units/?ids%5B%5D="
COURSE_URL = f"https://stepik.org/api/courses/"
ATTEMPT_URL = f"https://stepik.org/api/attempts?step=$solution_id&user=$user_id"
GET_ATTEMPT_URL = f"https://stepik.org/api/attempts"
SUBMIT_URL = f"https://stepik.org/api/submissions"
SOLUTION_URL = f"https://raw.githubusercontent.com/JustATRIK/lms_yandex/master/Stepik/plain/$step_id.json"
LESSON_URL = f"https://stepik.org/api/lessons?ids%5B%5D=$lesson_id"
SUBMISSION_URL = f"https://stepik.org/api/submissions?order=desc&step=$solution_id&user=$user_id"

def validate_response(response, exit_on_fail=False):
    if response.status_code > 299 or response.status_code < 200:
        print("Error! Status code", response.status_code)
        print(response.text)
        if exit_on_fail:
            exit()
        return False
    return True


def get_section_url(section):
    return SECTION_URL + str(section)


def get_course_url(course):
    return COURSE_URL + str(course)


def get_lesson_url(lesson_id):
    return LESSON_URL.replace("$lesson_id", str(lesson_id))


def get_solution_url(step_id):
    return SOLUTION_URL.replace("$step_id", str(step_id))


def get_attempt_url(solution_id, user_id):
    return ATTEMPT_URL.replace("$solution_id", str(solution_id)).replace("$user_id", str(user_id))

def get_submission_url(solution_id, user_id):
    return SUBMISSION_URL.replace("$solution_id", str(solution_id)).replace("$user_id", str(user_id))

dotenv.load_dotenv()

session = requests.Session()
csrf = os.getenv("csrftoken")

session.cookies.set('tmr_lvid', os.getenv("tmr_lvid"))
session.cookies.set('tmr_lvidTS', os.getenv("tmr_lvidTS"))
session.cookies.set('sessionid', os.getenv("sessionid"))
session.cookies.set('sessionid', os.getenv("sessionid"))
session.cookies.set('csrftoken', csrf)
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
    response = json.loads(response.text)

    if len(response["lessons"]) == 0:
        continue

    problems = response["lessons"][0]["steps"]
    contest_name = response["lessons"][0]["title"]
    print(f"Found {len(problems)} problems in lesson {contest_name}")

    for problem_id in problems:
        solved = False
        problem_solutions = session.get(get_submission_url(problem_id, user_id))
        print(f"Receiving from url {get_submission_url(problem_id, user_id)}")
        if validate_response(problem_solutions, exit_on_fail=False):
            problem_solutions_json = json.loads(problem_solutions.text)
            for solution in problem_solutions_json["submissions"]:
                if solution["status"] == "correct":
                    reply = solution["reply"]
                    solved = True
                    break
            if solved:
                print("Already solved :D")
                continue


        response = session.post(GET_ATTEMPT_URL, json={"attempt": {
            "dataset_url": None,
            "status": None,
            "step": str(problem_id),
            "time": None,
            "time_left": None,
            "user": None,
            "user_id": None,
        }}, headers={
            "x-csrftoken": csrf,
            "referer": "https://stepik.org/lesson/",
        })
        if not validate_response(response, exit_on_fail=False):
            continue

        attempt_data = json.loads(response.text)
        attempt_id = attempt_data["attempts"][0]["id"]

        print(get_solution_url(problem_id))
        solution_response = session.get(get_solution_url(problem_id))
        if not validate_response(solution_response, exit_on_fail=False):
            print("Probably not solved yet. Skipping...")
            continue

        solution_data = json.loads(solution_response.text)
        print(f"Loaded solution data {solution_data}")
        solution = solution_data["reply"]

        if "dataset" in solution_data:
            solution_by_choice = {solution_data["dataset"][i]: solution_data["reply"]["choices"][i] for i in range(len(solution_data["dataset"]))}
            print(solution_by_choice)

            problem_attempts = session.get(get_attempt_url(problem_id, user_id))
            if not validate_response(problem_attempts, exit_on_fail=False):
                continue

            dataset = ""
            for attempt in json.loads(problem_attempts.text)["attempts"]:
                print(attempt)
                if attempt["id"] == attempt_id:
                    dataset = attempt["dataset"]["options"]

            if dataset == "":
                print("Unable to load new dataset")
                continue

            choices = list(map(lambda x: solution_by_choice[x], dataset))
            solution = {"choices": choices}
            print(choices)

        response = session.post(SUBMIT_URL, json={"submission": {
            "attempt": str(attempt_id),
            "eta": None,
            "has_session": False,
            "hint": None,
            "reply": solution,
            "reply_url": None,
            "score": None,
            "session": None,
            "session_id": None,
            "status": None,
            "time": None,
        }}, headers={
            "x-csrftoken": csrf,
            "referer": "https://stepik.org/lesson/",
        })
        if not validate_response(response, exit_on_fail=False):
            continue

        print(f"Submitted solution. Status code {response.status_code}")
