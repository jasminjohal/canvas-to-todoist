from dotenv import load_dotenv
from canvasapi import Canvas
import os
import pandas as pd

load_dotenv()
API_URL = "https://canvas.oregonstate.edu/"
API_KEY = os.environ.get("CANVAS_KEY")
canvas = Canvas(API_URL, API_KEY)


def get_course_assignments(course_ID):
    course = canvas.get_course(course_ID)
    assignments = course.get_assignments()
    print(f'Processing tasks for {course.name}...')
    return assignments


def transform_assignments_to_df(assignments):
    dates = []
    tasks = []

    for assignment in assignments:
        tasks.append(assignment.name)
        dates.append(assignment.due_at)

    df = pd.DataFrame({'Tasks': tasks, 'Dates': dates})
    return df


def process_df_for_todoist(df):
    df = df.sort_values(by=['Dates'])
    df = df.rename(columns={"Dates": "DATE", "Tasks": "CONTENT"})

    # requisite columns for Todoist import
    df['TYPE'] = "task"
    df['PRIORITY'] = 4
    df['INDENT'] = ""
    df['AUTHOR'] = ""
    df['RESPONSIBLE'] = ""
    df['DATE_LANG'] = "en"
    df['TIMEZONE'] = ""

    # reorder columns and output to csv
    df = df[['TYPE', 'CONTENT', 'PRIORITY', 'INDENT', 'AUTHOR',
            'RESPONSIBLE', 'DATE', 'DATE_LANG', 'TIMEZONE']]

    return df


if __name__ == "__main__":
    courses = {'cs362': 1849691, 'cs325': 1784199, 'cs361': 1877222}
    course_ID = courses['cs361']
    assignments = get_course_assignments(course_ID)
    df = transform_assignments_to_df(assignments)
    df = process_df_for_todoist(df)
    df.to_csv(f'test.csv')
    print('Processing complete!')
