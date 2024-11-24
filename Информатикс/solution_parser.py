import json
import os
from pathlib import Path

import dotenv
import requests
from bs4 import BeautifulSoup

TARGET_LESSONS = [78011, 78558, 78807]
BASE_PATH = Path("./")
GROUP_ID = 5141

SOLUTION_URL = f"https://informatics.msk.ru/py/problem/run/$solution_id/source"
LESSON_URL = f"https://informatics.msk.ru/mod/statements/view.php?id=lesson_id#1"
PROBLEM_SOLUTIONS_URL = f"https://informatics.msk.ru/py/problem/$problem_id/filter-runs?problem_id=$problem_id&from_timestamp=-1&to_timestamp=-1&user_id=886144&lang_id=-1&status_id=0&statement_id=0&count=10&with_comment=&page=1&course_id={GROUP_ID}&group_id=0"


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
    return LESSON_URL.replace("lesson_id", str(lesson_id))


def get_problem_solutions_url(problem_id):
    return PROBLEM_SOLUTIONS_URL.replace("$problem_id", str(problem_id))


def get_solution_url(solution_id):
    return SOLUTION_URL.replace("$solution_id", str(solution_id))


dotenv.load_dotenv()
session = requests.Session()
session.cookies.set('MoodleSession', os.getenv("MoodleSession"))
session.cookies.set('cf_clearance', os.getenv("cf_clearance"))
session.headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                   "accept-encoding": "gzip, deflate, br, zstd", "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

for lesson_id in TARGET_LESSONS:
    response = session.get(get_lesson_url(lesson_id))
    bs = BeautifulSoup(response.text, "html.parser")

    contest_name = bs.find('h1').text
    internal_problem_id = list(filter(lambda x: "Задача №" in x.text, bs.findAll('h4')))[0].text
    internal_problem_id = internal_problem_id[internal_problem_id.index('№') + 1:internal_problem_id.index('.')]
    problems = [internal_problem_id]
    for link in map(lambda x: x["href"], bs.findAll('a', href=True)):
        if f"view.php?id={lesson_id}&chapterid=" in link:
            problems.append(link.split("=")[-1])
    print(f"Found {len(problems)} problems in lesson {contest_name}")

    id_s = 0
    for problem_id in problems:
        id_s += 1
        problem_solutions = session.get(get_problem_solutions_url(problem_id),
            headers={"content-type": "application/json", "accept": "*/*", "accept-encoding": "gzip, deflate, br, zstd", "content-encoding": "zstd"})
        if not validate_response(problem_solutions, exit_on_fail=False):
            continue

        problem_solutions_json = json.loads(problem_solutions.text)
        if problem_solutions_json["metadata"]["count"] < 1:
            continue

        problem_name = problem_solutions_json["data"][0]["problem"]["name"]
        solution_id = problem_solutions_json["data"][0]["id"]

        solution_code_response = session.get(get_solution_url(solution_id))
        if not validate_response(solution_code_response, exit_on_fail=False):
            continue

        solution_save_path = (BASE_PATH / format_path_dir(contest_name) / f"({id_s}) {format_path_dir(problem_name)}.py")
        solution_save_path.parent.mkdir(exist_ok=True, parents=True)
        if solution_save_path.exists():
            os.remove(solution_save_path)

        with open(solution_save_path, "a", encoding="utf-8") as file:
            data = json.loads(solution_code_response.text)["data"]["source"].splitlines()
            file.write("\n".join(data))
            file.flush()
        print(f"Saved ({id_s}/{len(problems)}):", solution_save_path)

