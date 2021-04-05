import pandas as pd

df = pd.read_csv('employees.csv')
total_earned = lambda row: row.hours_worked * row.hourly_wage if row.hours_worked <= 40 else row.hourly_wage * 40 + (row.hours_worked - 40) * row.hourly_wage * 1.5

df["total_earned"] = df.apply(total_earned, axis = 1)

print(df)
