from movies import movie_dataset, movie_ratings
from sklearn.neighbors import KNeighborsRegressor

regressor = KNeighborsRegressor(
  n_neighbors = 5,
  weights = "distance"  # "distance" or "uniform"
)

regressor.fit(
  movie_dataset,
  movie_ratings
)

unknown_ratings = [
  [0.016, 0.300, 1.022],         # Incredibles 2
  [0.0004092981, 0.283, 1.0112], # The Big Sick
  [0.00687649, 0.235, 1.0112]    # The Greatest Showman
]
guesses = regressor.predict(unknown_ratings)
print(guesses)

