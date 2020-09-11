from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# create a 2D visualisation
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y)
plt.show()

# Create a 3D Visualization
fig_3d = plt.figure()
constellation3d = fig_3d.add_subplot(1, 1, 1, projection = "3d")
constellation3d.scatter(x, y ,z)
plt.show()

# Stars within 10 light-years of our Sun:
sx = [-1.643, -0.0566, -7.416, -6.523, 7.417, -1.612, 1.912, 0]
sy = [-1.374, -5.920, 2.193, 1.646, 3.318, 8.078, -8.658, 0]
sz = [-3.838, 0.486, 0.993, 4.882, -2.673, -2.474, -3.917, 0]
stars = ["Alpha and Proxima Centauri", "Barnard's Star", "Wolf 359", "Lalande 21185", "UV Ceti", "Sirius", "Ross 154", "Sol"]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(sx, sy)

for x_pos, y_pos, label in zip(sx, sy, stars):
    ax.annotate(label,             # The label for this point
                xy = (x_pos, y_pos), # Position of the corresponding point
                xytext = (7, 0),     # Offset text by 7 points to the right
                textcoords = 'offset points', # tell it to use offset points
                ha = 'left',         # Horizontally aligned to the left
                va = 'center')       # Vertical alignment is centered


plt.title("Stars within 10 light-years of our Sun:")
plt.xlabel("Light-year")
plt.ylabel("Light-year")
plt.show()

fig_3d = plt.figure()
constellation3d = fig_3d.add_subplot(1, 1, 1, projection = "3d")
"""
constellation3d.scatter(sx, sy ,sz)
"""
constellation3d.set_xlabel("Light-year")
constellation3d.set_ylabel("Light-year")
constellation3d.set_zlabel("Light-year")


for i in range(len(stars)):
    constellation3d.scatter(sx[i], sy[i], sz[i], color = "blue")
    constellation3d.text(sx[i], sy[i], sz[i], "%s" % ("  " + stars[i]), zorder=1)


plt.title("Stars within 10 light-years of our Sun:")
plt.show()
