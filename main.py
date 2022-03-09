from dotenv import load_dotenv
from canvasapi import Canvas
import os
import pandas as pd

load_dotenv()
API_URL = "https://canvas.oregonstate.edu/"
API_KEY = os.environ.get("CANVAS_KEY")

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(1849691)  # cs362?
# course = canvas.get_course(1784199)  # cs325
# course = canvas.get_course(1877222)  # cs361
print(course.name)

dates = []
tasks = []
times = []

assignments = course.get_assignments()

for assignment in assignments:
    tasks.append(assignment.name)
    dates.append(assignment.due_at)

syllabus_df = pd.DataFrame(
    {'Tasks': tasks, 'Dates': dates})

df = syllabus_df.sort_values(by=['Dates'])

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

df.to_csv('test.csv')
