import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
print("___ Load the Data ___")
passengers = pd.read_csv("passengers.csv")
#print(passengers.head())
#print(passengers.columns)
#print(passengers.describe())
#print(passengers.info())

print("___ Clean the Data ___")
# Update sex column to numerical
#print(set(passengers.Sex))
#print(passengers.Sex)
passengers.replace("female", 1, inplace = True)
passengers.replace("male", 0, inplace = True)
#print(passengers.Sex)

# Fill the nan values in the age column
#print(passengers.Age)
age_mean = int(passengers.Age.mean())
passengers.Age.fillna(
    value = age_mean,
    inplace = True
)
#print(passengers.Age)

# Create a first class column
add_class = lambda row, p_class: 1 if row == p_class else 0

#print(passengers.Pclass)
#print(set(passengers.Pclass))
passengers["FirstClass"] = passengers.Pclass.apply(add_class, args = (1,))
#print(passengers.head())

# Create a second class column
passengers["SecondClass"] = passengers.Pclass.apply(add_class, args = (2,))
#print(passengers.tail())

# Select the desired features
print("___ Select and Split the Data ___")
features = passengers[["Sex", "Age", "FirstClass", "SecondClass"]]
#print(features.head())
survival = passengers.Survived
#print(type(survival))
#print(survival.head())

# Perform train, test, split
X_train, X_test, y_train, y_test = train_test_split(
    features,
    survival,
    test_size = 0.2,
    random_state = 1
)

# Scale the feature data so it has mean = 0 and standard deviation = 1
print("___ Normalize the Data ___")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the model
print("___ Create and Evaluate the Model ___")
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Score the model on the train data
train_score = model.score(X_train_scaled, y_train)     # The score returned is the percentage of correct classifications, or the accuracy.
print("Train score: ",train_score)

# Score the model on the test data
test_score = model.score(X_test_scaled, y_test)
print("Test score: ", test_score)

# Analyze the coefficients
coeff = model.coef_     # a vector of the coefficients of each feature
#print("Coefficients: ", coeff)
print(list(zip(X_train.columns, model.coef_[0])))
print("The Sex feauter is the most important in predicting survival on the sinking of the Titanic.")

print("___ Predict with the Model ___")
# Sample passenger features
Jack = np.array([
  0.0,    # Sex
  20.0,   # Age
  0.0,    # FirstClass
  0.0     # SecondClass
])
Rose = np.array([
  1.0,
  17.0,
  1.0,
  0.0
])
You = np.array([
  0.0,
  48.0,
  0.0,
  0.0
])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengers_scaled = scaler.transform(sample_passengers)
#print(sample_passengers_scaled)

# Make survival predictions!
prediction = model.predict(sample_passengers_scaled)
print("Predictions: ", prediction)

probabilities = model.predict_proba(sample_passengers_scaled)
print("Probabilities:", probabilities)

x = range(len(sample_passengers))
y = probabilities[:, 1]
plt.bar(
  x,
  y * 100
)
plt.yticks(np.arange(0, 101, 25), ("0%", "25%", "50%", "75%", "100%"))
plt.xticks(np.arange(3), ("Jack", "Rose", "You"))
plt.title("Chance to survive the Titanic")

plt.show()
