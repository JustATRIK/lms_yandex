import json
import os
from pathlib import Path

import dotenv
import requests
from bs4 import BeautifulSoup

TARGET_LESSONS = [663328]
BASE_PATH = Path("./")
GROUP_ID = 5141

REQUEST_ATTEMPT_URL = "https://stepik.org/api/attempts"
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
session.cookies.set('csrftoken', os.getenv("csrftoken"))
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

    for problem_numeric_id, problem_id in enumerate(problems, 1):
        headers = dict(session.headers)
        headers["referer"] = f"https://stepik.org/lesson/{lesson_id}/step/{problem_numeric_id}?unit=661015"
        headers["x-csrftoken"] = session.cookies["csrftoken"]
        attempt_req = session.get(REQUEST_ATTEMPT_URL, data={"attempt": {
            "status": None,
            "dataset_url": None,
            "step": str(problem_id),
            "time": None,
            "time_left": None,
            "user": None,
            "user_id": None
        }}, headers=headers)
        attempt_data = json.loads(attempt_req.text)
        attempt_id = -1
        for attempt in attempt_data["attempts"]:
            if attempt["status"] == "active":
                attempt_id = attempt["id"]
        if attempt_id == -1:
            continue


