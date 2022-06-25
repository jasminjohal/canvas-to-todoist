from dotenv import load_dotenv
from canvasapi import Canvas
import os
from todoist_api_python.api import TodoistAPI

load_dotenv()
API_URL = "https://canvas.oregonstate.edu/"
CANVAS_KEY = os.environ.get("CANVAS_KEY")
canvas = Canvas(API_URL, CANVAS_KEY)
TODOIST_KEY = os.environ.get("TODOIST_KEY")


def get_course_assignments(course_ID):
    course = canvas.get_course(course_ID)
    assignments = course.get_assignments()
    print(f'Processing tasks for {course.name}...')
    return assignments


def add_tasks_to_todoist(assignments, verbosity):
    api = TodoistAPI(TODOIST_KEY)
    project_name = input(
        "What would you like to name the project in Todoist? ")
    try:
        project = api.add_project(name=project_name)
    except Exception as error:
        print(error)

    for assignment in assignments:
        try:
            task = api.add_task(
                content=assignment.name,
                due_datetime=assignment.due_at,
                project_id=project.id)
            if verbosity:
                print(f'Added task \'{task.content}\' to {project.name}')
        except Exception as error:
            print(error)


if __name__ == "__main__":
    # courses = {'cs362': 1849691, 'cs325': 1784199,
    #            'cs361': 1877222, 'cs493': 1870359}
    # course_ID = courses['cs493']
    course_ID = int(input("Enter in a course ID: "))
    assignments = get_course_assignments(course_ID)
    add_tasks_to_todoist(assignments, verbosity=True)
    print('Processing complete!')
