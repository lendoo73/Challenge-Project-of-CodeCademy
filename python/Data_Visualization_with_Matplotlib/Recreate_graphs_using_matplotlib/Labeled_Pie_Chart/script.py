import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here
# 1:
plt.figure(figsize = [10, 8])
# 2, 4:
plt.pie(num_hardest_reported, autopct = "%1d%%", labels = unit_topics)
# 3:
plt.axis("equal")
# 5:
plt.title("Hardest Topics")
# 6:
plt.savefig("my_pie_chart.png")
plt.show()
