import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets

# From sklearn.cluster, import KMeans class
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(
  n_clusters = 3
)

# Use .fit() to fit the model to samples
model.fit(samples)

# Use .predict() to determine the labels of samples 
labels = model.predict(samples)

# Print the labels
print(labels)
