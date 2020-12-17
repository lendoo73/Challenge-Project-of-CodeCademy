import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd

iris = datasets.load_iris()

samples = iris.data

target = iris.target

model = KMeans(n_clusters=3)

model.fit(samples)

labels = model.predict(samples)

# Code starts here:
species = np.chararray(target.shape, itemsize=150)

name = [
  "setosa",
  "versicolor",
  "virginica"
]
for i in range(len(samples)):
  species[i] = name[target[i]]

df = pd.DataFrame({
  "labels": labels,
  "species": species
})
print(df)

ct = pd.crosstab(df.labels, df.species)
print(ct)

