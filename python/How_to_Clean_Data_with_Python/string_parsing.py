import pandas as pd
from students import students

students["score"] = students.score.replace(
    "%", 
    "", 
    regex = True
)
students.score = pd.to_numeric(students.score)
print(students.head())
