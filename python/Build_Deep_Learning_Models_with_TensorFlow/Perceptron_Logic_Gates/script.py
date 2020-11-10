import seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1]
]

labels_AND = [0, 0, 0, 1]
labels_XOR = [0, 1, 1, 0]
labels_OR = [0, 1, 1, 1]

def visualise_gate(labels, name = ""):

    x = [point[0] for point in data]
    y = [point[1] for point in data]

    classifier = Perceptron(
    max_iter = 40
    )

    classifier.fit(data, labels)
    print(f"{name} gate: ", classifier.score(data, labels))
    result = classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]])
    print(result)

    # make a heat map that reveals the decision boundary:
    #  a list of 100 evenly spaced decimals between 0 and 1:
    x_values = y_values = np.linspace(0, 1, 100)
    point_grid = list(product(x_values, y_values))
    distances = classifier.decision_function(point_grid )
    abs_distances = np.abs(distances)
    distances_matrix = abs_distances.reshape((100, 100))

    plt.scatter(x, y, c = labels)
    plt.title(f"{name} gate")
    plt.show()

    heatmap = plt.pcolormesh(
        x_values,
        y_values,
        distances_matrix,
        shading='auto'
    )
    plt.colorbar(heatmap)
    plt.show()

visualise_gate(labels_AND, "AND") 
visualise_gate(labels_XOR, "XOR") 
visualise_gate(labels_OR, "OR") 
