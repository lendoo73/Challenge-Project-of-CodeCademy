import pandas as pd

students = pd.read_csv("students.csv")
students = students[['full_name', 'gender_age','fractions','probability','grade']]
