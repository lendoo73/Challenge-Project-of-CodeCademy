import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns = ['month', 'clinic_east', 'clinic_north', 'clinic_south', 'clinic_west']
)

january_february_march = df[df.month.isin([
  "January", 
  "February",
  "March"
])]
print(january_february_march)
