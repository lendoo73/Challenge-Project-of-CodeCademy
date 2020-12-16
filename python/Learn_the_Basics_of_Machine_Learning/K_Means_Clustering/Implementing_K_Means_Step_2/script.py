import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids

k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

# Step 2: Assign samples to nearest centroid

# Distance formula
def equal_dimension(a, b):
  if len(a) == len(b):
    return True

def distance(a, b):
  if not equal_dimension(a, b):
    return "ERROR: Different number of dimensions!"
  distance = 0
  # loop throw the dimensions
  for i in range(len(a)):
    difference = (b[i] - a[i]) ** 2
    distance += difference
  
  return distance ** 0.5

# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))

# Distances to each centroid
distances = np.zeros(k)

for i in range(len(samples)):
  
  distances[0] = distance(sepal_length_width[i], centroids[0])
  
  distances[1] = distance(sepal_length_width[i], centroids[1])
  
  distances[2] = distance(sepal_length_width[i], centroids[2])
  
  # Assign to the closest centroid
  cluster = np.argmin(distances)
  labels[i] = cluster


# Print labels
print(labels)
