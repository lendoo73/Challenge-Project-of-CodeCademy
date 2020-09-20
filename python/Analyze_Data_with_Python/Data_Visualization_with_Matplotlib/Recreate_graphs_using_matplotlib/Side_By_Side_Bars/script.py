import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here
# 1:
t = 2 # There are two sets of data: A and B
w = 0.8 # We generally want bars to be 0.8
n = 1 # A is first set of data
d = 5 # There are 5 topics we're plotting
school_a_x = create_x(t, w, n, d)
n = 2
school_b_x = create_x(t, w, n, d)
# 2:
plt.figure(figsize = [10, 8])
# 3:
ax = plt.subplot()
# 4:
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
# 5:
middle_x = [(a + b) / 2 for a, b in zip(school_a_x, school_b_x)]
# 6:
ax.set_xticks(middle_x)
# 7:
ax.set_xticklabels(unit_topics, fontsize = 14, rotation = "vertical")
# 8:
plt.legend(["Middle School A", "Middle School B"], fontsize = 20, loc = 5)
plt.title("Test Averages on Different Units", fontsize = 20)
plt.xlabel("Unit", fontsize = 16)
plt.ylabel("Test Average", fontsize = 16)
plt.savefig("my_side_by_side.png")
plt.show()
