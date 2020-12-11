import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

breast_cancer_data = load_breast_cancer()

model = LogisticRegression()
model.fit(breast_cancer_data.data,breast_cancer_data.target)

coefficients = model.coef_
coefficients = coefficients.tolist()[0]
print(coefficients)
print(len(coefficients))


# Plot bar graph
plt.bar(range(len(breast_cancer_data.feature_names)), coefficients)
plt.xticks(range(len(breast_cancer_data.feature_names)), breast_cancer_data.feature_names, rotation = "vertical")
plt.xlabel('feature')
plt.ylabel('coefficient')
 
plt.show()
