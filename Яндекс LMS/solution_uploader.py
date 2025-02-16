import json
import os
import dotenv
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def get_lesson_url(lesson_id):
    return lesson_url.replace("lesson_id", str(lesson_id))

def validate_response(response, exit_on_fail=False):
    if response.status_code != 200:
        print("Error! Status code", response.status_code, response.url)
        print(response.text)
        if exit_on_fail:
            exit()
        return False
    return True


course_id = 957
group_id = 43114
solution_url = f"https://raw.githubusercontent.com/JustATRIK/lms_yandex/master/%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20LMS/{course_id}"
lesson_url = f"https://lms.yandex.ru/api/student/lessonTasks?courseId={course_id}&groupId={group_id}&lessonId=lesson_id"
solution_to_upl_url = f"https://lms.yandex.ru/api/student/tasks/$problem_id?groupId={group_id}"
solution_upl_url = f"https://lms.yandex.ru/api/student/solutions/$solution_url/comments/files"

dotenv.load_dotenv()
session = requests.Session()
session.max_redirects = 1000
csrftoken = os.getenv("csrftoken")
session.cookies.set('Session_id', os.getenv("session_id"))
session.cookies.set('csrftoken', csrftoken)
session.headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "content-type": "application/json",
                   "accept-encoding": "gzip, deflate, br, zstd", "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

lessons = list(map(int, input().split()))
for lesson_id in lessons:
    response = session.get(get_lesson_url(lesson_id))
    validate_response(response, exit_on_fail=True)

    for lesson_type in json.loads(response.text):
        lesson = lesson_type["tasks"][0]["lesson"]

        print(f"Found {len(lesson_type['tasks'])} problems in lesson {lesson_id}")
        total_count = len(lesson_type['tasks'])
        for index, problem in enumerate(lesson_type["tasks"], start=1):
            problem_id = problem['id']
            code = requests.get(solution_url + f"/{lesson_id}/{problem_id}.py")
            if not validate_response(code, exit_on_fail=False):
                print("Probably problem isn't solved yet! Skipping...")
                continue
            code = code.text

            problem_data = session.get(solution_to_upl_url.replace("$problem_id", str(problem_id)))
            if not validate_response(problem_data, exit_on_fail=False):
                continue

            problem_data = json.loads(problem_data.text)
            solution_to_upl_id = problem_data['solutionId']
            multipart_data = MultipartEncoder(
                fields={"file": ("solution.py", code, "text/x-python")},
                boundary="----WebKitFormBoundary4LH1AXvtFuyNM6mB"
            )
            upload_request = session.post(solution_upl_url.replace('$solution_url', str(solution_to_upl_id)), data=multipart_data, headers={
                    "content-type": multipart_data.content_type,
                    "x-csrf-token": csrftoken
                })
            percentage = int(index / total_count * 20)
            print('\r', end='')
            print(f"Problem {problem_id} ({index}/{total_count}): [{'=' * percentage}{'.' * (20 - percentage)}]", end='')
            print('\r', end='')
        print()