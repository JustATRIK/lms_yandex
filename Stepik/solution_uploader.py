import json
import os
from pathlib import Path

import dotenv
import requests
from bs4 import BeautifulSoup

TARGET_LESSONS = [669829]
BASE_PATH = Path("./")
GROUP_ID = 5141

GET_ATTEMPT_URL = f"https://stepik.org/api/attempts"
SUBMIT_URL = f"https://stepik.org/api/submissions"
SOLUTION_URL = f"https://raw.githubusercontent.com/JustATRIK/lms_yandex/master/Stepik/plain/$step_id.json"
LESSON_URL = f"https://stepik.org/api/lessons?ids%5B%5D=$lesson_id"

def validate_response(response, exit_on_fail=False):
    if response.status_code > 299 or response.status_code < 200:
        print("Error! Status code", response.status_code)
        print(response.text)
        if exit_on_fail:
            exit()
        return False
    return True

def get_lesson_url(lesson_id):
    return LESSON_URL.replace("$lesson_id", str(lesson_id))


def get_solution_url(step_id):
    return SOLUTION_URL.replace("$step_id", str(step_id))


dotenv.load_dotenv()

session = requests.Session()
csrf = os.getenv("csrftoken")

session.cookies.set('tmr_lvid', os.getenv("tmr_lvid"))
session.cookies.set('tmr_lvidTS', os.getenv("tmr_lvidTS"))
session.cookies.set('sessionid', os.getenv("sessionid"))
session.cookies.set('sessionid', os.getenv("sessionid"))
session.cookies.set('csrftoken', csrf)
user_id = os.getenv("user_id")

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

        solution_response = session.get(get_solution_url(problem_id))
        if not validate_response(solution_response, exit_on_fail=False):
            print("Probably not solved yet. Skipping...")
            continue

        solution = json.loads(solution_response.text)
        print(f"Loaded solution {solution}")

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
