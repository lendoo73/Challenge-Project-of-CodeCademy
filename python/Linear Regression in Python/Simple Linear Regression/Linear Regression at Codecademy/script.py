# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)
# Show then clear plot
plt.show()
plt.clf()


# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula(
  "score ~ completed",
  data = codecademy
)
result = model.fit()
print(result.params)

# Intercept interpretation:
print("A learner who has previously completed 0 content items is expected to earn a quiz score of 13.2 points.")

# Slope interpretation:
print("Students who have completed one additional prior content item are expected to score 1.3 points higher on the quiz.")

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, result.predict(codecademy))

# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
print(result.predict({'completed':[20]}))
intercept = result.params[0]
slope = result.params[1]
print(slope * 20 + intercept)

# Calculate fitted values
fitted_values = result.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(
  data = codecademy,
  x = "lesson",
  y = "score"
)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula(
  "score ~ lesson",
  data = codecademy
)
result = model.fit()
print(result.params)


# Calculate and print the group means and mean difference (for comparison)
mean_score_lessonA = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
mean_score_lessonB = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
print('Mean score (A): ', mean_score_lessonA)
print('Mean score (B): ', mean_score_lessonB)
print('Mean score difference: ', mean_score_lessonA - mean_score_lessonB)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(
  x = "completed",
  y = "score",
  hue = "lesson",
  data = codecademy
)

plt.show()
plt.clf()
