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

# Testing Your Model:
new_samples = np.array(
[
[0.00,0.38,4.12,4.57,3.89,3.81,1.07,0.00,0.00,2.59,7.40,4.80,5.34,5.34,1.68,0.00,0.00,2.75,7.32,4.57,4.42,1.83,0.00,0.00,0.00,2.29,6.56,4.88,5.80,7.63,2.36,0.00,0.00,0.00,0.00,0.00,0.23,6.41,3.81,0.00,0.00,2.75,4.27,4.81,7.02,7.32,1.83,0.00,0.00,2.36,5.95,5.41,3.20,0.69,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.46,2.06,0.00,0.00,0.00,0.00,0.00,3.13,6.94,7.09,0.46,0.00,0.00,0.00,1.75,7.63,3.89,0.30,0.00,0.00,0.00,0.00,4.42,6.33,2.29,1.83,0.00,0.00,0.00,0.00,4.57,7.62,7.17,7.63,3.43,0.00,0.00,0.00,3.13,7.32,2.52,5.04,6.86,0.00,0.00,0.00,0.38,6.10,7.32,7.63,5.34,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.30,3.05,1.83,0.00,0.00,0.00,0.00,3.36,6.79,7.62,4.27,0.00,0.00,0.00,5.04,7.47,3.89,7.09,2.59,0.00,0.00,0.00,1.98,1.15,0.00,6.86,2.29,0.00,0.00,0.00,0.00,0.00,0.00,6.86,2.29,0.00,0.00,0.00,0.00,0.00,0.00,6.86,2.29,0.00,0.00,0.00,0.00,0.00,0.00,2.29,0.46,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,1.37,3.74,3.81,3.43,0.23,0.00,0.00,0.00,5.11,6.71,5.34,7.62,1.52,0.00,0.00,0.00,5.95,6.41,4.65,7.62,1.53,0.00,0.00,0.00,2.60,7.62,7.32,7.63,4.88,0.69,0.00,0.00,5.72,5.65,0.76,3.66,7.32,2.29,0.00,1.14,7.62,3.66,1.52,1.75,7.24,2.29,0.00,0.53,5.80,7.47,7.62,7.63,6.48,0.69,0.00,0.00,0.00,0.00,0.31,0.23,0.00,0.00,0.00]
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
