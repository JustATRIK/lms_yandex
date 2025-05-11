import os
from pathlib import Path
import dotenv
import requests
import json

IGNORE_LESSONS = [5217]
TARGET_LESSONS = [5174]
BASE_PATH = Path("./")
LESSON_NAME_BY_TYPE = {
    "classwork": "Классная работа",
    "homework": "Домашняя работа",
    "additional": "Доп задачи",
    "individual-work": "Контрольная работа",
    "control-work": "Контрольная работа"
}

course_id = 957
group_id = 43114
lesson_ids_url = f"https://lms.yandex.ru/api/student/lessons?courseId={course_id}&groupId={group_id}"
lesson_url = f"https://lms.yandex.ru/api/student/lessonTasks?courseId={course_id}&groupId={group_id}&lessonId=lesson_id"
solution_url = f"https://lms.yandex.ru/api/student/solutions/solution_id/comments-v2?courseId={course_id}&groupId={group_id}"


def validate_response(response, exit_on_fail=False):
    if response.status_code != 200:
        print("Error! Status code", response.status_code)
        print(response.text)
        if exit_on_fail:
            exit()
        return False
    return True


def format_path_dir(path_dir):
    return path_dir.replace(".", "").replace(":", "").replace("?", "").replace("!", "").replace(",", "")


def get_lesson_url(lesson_id):
    return lesson_url.replace("lesson_id", str(lesson_id))


def get_solution_url(solution_id):
    return solution_url.replace("solution_id", str(solution_id))


def found_valid_solution(submissions):
    for sub in submissions:
        if sub["submission"] is not None and sub["submission"]["contestScore"] is not None and sub["submission"]["contestScore"] >= 100:
            return sub
    return None


dotenv.load_dotenv()
session = requests.Session()
session.max_redirects = 1000
session.cookies.set('Session_id',
                    os.getenv("session_id"))
session.headers = {"accept": "application/json", "content-type": "application/json",
                   "accept-encoding": "gzip, deflate, br, zstd"}

lessons = []
if not TARGET_LESSONS:
    group_lessons_response = session.get(lesson_ids_url)
    validate_response(group_lessons_response, exit_on_fail=True)
    for group_lesson in json.loads(group_lessons_response.text):
        lesson_id = group_lesson["id"]
        if lesson_id in IGNORE_LESSONS:
            continue
        lessons.append(lesson_id)
else:
    lessons = TARGET_LESSONS

for lesson_id in lessons:
    response = session.get(get_lesson_url(lesson_id))
    validate_response(response, exit_on_fail=True)

    for lesson_type in json.loads(response.text):
        lesson = lesson_type["tasks"][0]["lesson"]
        lesson_name = lesson["title"]

        task_id = 0
        print(f"Found {len(lesson_type['tasks'])} problems in lesson {lesson_name}: {LESSON_NAME_BY_TYPE[lesson_type['type']]}")
        for problem in lesson_type["tasks"]:
            task_id += 1

            problem_name = problem["title"]
            problem_id = problem["id"]
            solution = problem["solution"]
            if solution is None:
                continue
            solution_id = solution["id"]
            solution_type = solution["status"]["type"]
            if solution_type == "accepted":
                solution_data = found_valid_solution(json.loads(session.get(get_solution_url(solution_id)).text)["comments"])
                if solution_data is None:
                    continue
                solution_file_url = solution_data["files"][0]["url"]
                file_data = session.get(solution_file_url)

                auto_upload_save_path = (BASE_PATH / "plain" / f"{problem_id}.py")
                solution_save_path = (BASE_PATH / format_path_dir(lesson_name) / LESSON_NAME_BY_TYPE[lesson_type["type"]] /
                                      f"({task_id}) {format_path_dir(problem_name)}.py")
                solution_save_path.parent.mkdir(exist_ok=True, parents=True)
                if solution_save_path.exists():
                    os.remove(solution_save_path)

                auto_upload_save_path.parent.mkdir(exist_ok=True, parents=True)
                if auto_upload_save_path.exists():
                    os.remove(auto_upload_save_path)

                with open(solution_save_path, "a", encoding="utf-8") as file:
                    file.write(file_data.text)
                    file.flush()
                with open(auto_upload_save_path, "a", encoding="utf-8") as file:
                    file.write(file_data.text)
                    file.flush()
                print(f"Saved ({task_id}/{len(lesson_type['tasks'])}):", solution_save_path)
