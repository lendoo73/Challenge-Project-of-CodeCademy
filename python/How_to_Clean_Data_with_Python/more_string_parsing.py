import pandas as pd
from students import students

students.grade = students.grade.replace(
    "(\D+)", 
    "", 
    regex = True
)

students.grade = pd.to_numeric(students.grade)

avg_grade = students.grade.mean()

print(avg_grade)
