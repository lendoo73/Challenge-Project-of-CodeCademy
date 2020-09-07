import codecademylib
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
# 1:
plt.figure(figsize = [10, 8])
# 2 - 3:
plt.bar(range(len(past_years_averages)), past_years_averages, yerr = error)
# 4:
plt.axis([-0.5, 6.5, 70, 95])
# 5:
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
# 6:
plt.title("Final Exam Averages", fontsize = 20)
plt.xlabel("Year", fontsize = 20)
plt.ylabel("Test average", fontsize = 20)
# 7:
plt.savefig("my_bar_chart.png")
plt.show()
