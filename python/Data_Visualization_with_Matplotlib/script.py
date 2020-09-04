import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
# 3:
plt.figure(figsize = (12, 8))
# 4: (number of rows: 1, number of columns: 2, index of the curremt plot: 1)
ax1 = plt.subplot(1, 2, 1)
# 6:
x_values = range(len(months))
# 7-8:
plt.plot(x_values, visits_per_month, marker = "o")
# 9:
plt.xlabel("Months")
plt.ylabel("Visitors")
# 10:
ax1.set_xticks(x_values)
# 11:
ax1.set_xticklabels(months)
# 16:
plt.title("Page Visits Per Month")

# 5:
ax2 = plt.subplot(1, 2, 2)
# 12-13:
plt.plot(x_values, key_limes_per_month, color = "black")
plt.plot(x_values, persian_limes_per_month, color = "orange")
plt.plot(x_values, blood_limes_per_month, color = "red")
# 14:
plt.legend(["key limes", "persian limes", "blood limes"])
plt.xlabel("Month")
plt.ylabel("Limes sold")
# 15-16:
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title("Lime Sales Per Month")
plt.subplots_adjust(wspace = 0.3)

plt.show()
# 17:
plt.savefig("sublime_limes_line_graphs.png")
