import pandas as pd
from students import students

print(students)

duplicates = students.duplicated()

students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())
