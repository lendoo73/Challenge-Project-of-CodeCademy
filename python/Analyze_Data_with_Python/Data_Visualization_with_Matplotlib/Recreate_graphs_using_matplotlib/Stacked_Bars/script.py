import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
# 1:
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
# 2:
plt.figure(figsize = [10, 8])
#create your plot here
# 3:
x_length = range(len(unit_topics))
plt.bar(x_length, As)
plt.bar(x_length, Bs, bottom = As)
plt.bar(x_length, Cs, bottom = c_bottom)
plt.bar(x_length, Ds, bottom = d_bottom)
plt.bar(x_length, Fs, bottom = f_bottom)
# 4:
ax = plt.subplot()
# 5:
ax.set_xticks(x_length)
# 6:
ax.set_xticklabels(unit_topics)
# 7:
plt.title("Grade distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")
# 8:
plt.savefig("my_stacked_bar.png")
plt.show()
