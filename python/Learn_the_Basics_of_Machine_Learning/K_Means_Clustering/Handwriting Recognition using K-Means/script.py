import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
# Getting Started with the Digits Dataset:
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
#print(digits)
#print(digits.DESCR)
#print(digits.data)
print(digits.target[100])

# Figure size (width, height)
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots  
fig.subplots_adjust(
  left = 0, 
  right = 1, 
  bottom = 0, 
  top = 1, 
  hspace = 0.05, 
  wspace = 0.05
)
 
# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(
      8, 
      8, 
      i + 1, 
      xticks = [], 
      yticks = []
    )
 
    # Display an image at the i-th position
    ax.imshow(
      digits.images[i], 
      cmap = plt.cm.binary, 
      interpolation = 'nearest'
    )
 
    # Label the image with the target value
    ax.text(0, 7, str(digits.target[i]))
    
plt.show()

# K-Means Clustering:
model = KMeans(
  n_clusters = 10,
  random_state = 42
)

model.fit(digits.data)

# Visualizing after K-Means:
fig = plt.figure(figsize = (8, 3))
plt.suptitle(
  "Cluser Center Images",
  fontsize = 14,
  fontweight = "bold"
)

for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position:
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images:
  ax.imshow(
    model.cluster_centers_[i].reshape((8, 8)),
    cmap = plt.cm.binary
  )

plt.show()

# Testing Your Model: (0123)
new_samples = np.array(
[
[0.00,0.61,4.81,6.79,6.86,4.73,1.07,0.00,0.00,6.10,7.55,4.88,4.27,7.40,6.25,0.00,0.61,7.62,3.66,0.00,0.00,3.66,7.63,0.77,0.76,7.62,2.29,0.00,0.00,2.29,7.62,1.52,0.76,7.62,2.29,0.00,0.00,4.35,7.62,0.61,0.76,7.62,3.74,1.76,5.41,7.62,5.34,0.00,0.00,5.79,7.62,7.62,7.24,3.81,0.23,0.00,0.00,0.46,3.05,2.90,0.62,0.00,0.00,0.00],
[0.00,0.00,0.00,1.68,4.65,3.28,0.00,0.00,0.00,0.38,4.80,7.62,7.62,5.72,0.00,0.00,1.15,6.33,7.62,4.27,4.96,6.79,0.00,0.00,4.42,7.17,2.29,0.00,3.81,6.86,0.00,0.00,0.53,0.84,0.00,0.00,4.27,6.86,0.00,0.00,0.00,0.00,0.00,0.00,5.34,5.87,0.00,0.00,0.00,0.00,0.00,0.00,6.02,5.18,0.00,0.00,0.00,0.00,0.00,0.00,3.82,2.75,0.00,0.00],
[0.00,0.00,1.22,4.35,5.34,3.43,0.00,0.00,0.00,3.74,7.55,7.55,6.56,7.62,2.44,0.00,0.00,7.17,5.34,0.76,0.84,7.62,3.05,0.00,0.00,0.00,0.00,0.23,5.56,7.47,1.37,0.00,0.00,0.00,0.46,5.49,7.62,3.13,0.00,0.00,0.00,1.45,6.41,7.55,3.36,0.00,0.00,0.00,4.73,7.55,7.62,6.94,4.57,2.97,3.89,4.58,7.47,5.41,4.57,5.64,7.40,7.62,7.47,6.56],
[0.00,1.45,3.97,5.95,6.86,6.86,3.66,0.00,0.00,5.87,7.62,6.02,4.19,5.80,7.47,0.46,0.00,0.38,0.38,0.00,0.31,4.12,7.62,0.76,0.00,0.00,0.00,3.21,7.24,7.62,5.87,0.15,0.00,0.00,0.00,2.29,5.34,7.62,6.41,0.00,0.00,0.00,0.00,0.00,0.00,5.11,7.62,0.00,2.59,5.87,5.34,3.97,5.95,7.62,4.96,0.00,1.83,5.26,6.33,7.63,6.64,3.81,0.38,0.00]
]
)

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(3, end='')
  elif new_labels[i] == 1:
    print(0, end='')
  elif new_labels[i] == 2:
    print(8, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(9, end='')
  elif new_labels[i] == 5:
    print(2, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(7, end='')
  elif new_labels[i] == 8:
    print(6, end='')
  elif new_labels[i] == 9:
    print(5, end='')
