import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# 1:
#print(london_data.head())
# 2:
#print(len(london_data))
# 3:
temp = london_data["TemperatureC"]
#print(temp)
# 4:
average_temp = np.mean(temp)
#print(average_temp)
# 5:
temperature_var = np.var(temp)
#print(temperature_var)
# 6:
temperature_standard_deviation = np.std(temp)
#print(temperature_standard_deviation)
# 7:
#print(london_data.tail())
# 8:
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
#print(june)
# 9:
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
#print(july)
# 10:
average_june = np.mean(june)
average_july = np.mean(july)
#print(average_june)
#print(average_july)
# 11:
std_june = np.std(june)
std_july = np.std(july)
#print(std_june)
#print(std_july)
# 12:
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  #print("The mean temperature in month {} is {}".format(i, np.mean(month)))
  #print("The standard deviation of temperature in month {} is {} ".format(i, np.std(month)))
# 13/a:
rainest_month = 1
mean_rainMM = 0
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["dailyrainMM"]
  mean = np.mean(month)
  if mean > mean_rainMM:
    mean_rainMM = mean
    rainest_month = i
#print("The rainiest month in London is {}".format(rainest_month))
#print(mean_rainMM)

# 13/b:
rainest_month = 1
rainiest_hour = 0
mean_hourMM = 0
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]
  for h in range(0, 24):
    hour = month.loc[month["hour"] == h]["dailyrainMM"]
    mean = np.mean(hour)
    if mean > mean_hourMM:
      mean_hourMM = mean
      rainest_month = i
      rainiest_hour = h

#print("The rainest hour is {} in month {}".format(rainiest_hour, rainest_month))
#print(mean_hourMM)
# 13/c:
certain_hours = []
for h in range(0, 24):
  hour = london_data.loc[london_data["hour"] == h]["dailyrainMM"]
  var_hour = np.var(hour)
  if var_hour > 10:
    certain_hours.append(h)
print("Certain hours that have higher variance than others: ")  
print(* certain_hours, sep = ", ")

