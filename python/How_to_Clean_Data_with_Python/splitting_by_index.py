import pandas as pd
from students import students

print(students.columns)
print(students.head())
students["gender"] = students.gender_age.str[:1]
students["age"] = students.gender_age.str[1:]
students = students.drop(columns = ["gender_age"])
print(students.head())


