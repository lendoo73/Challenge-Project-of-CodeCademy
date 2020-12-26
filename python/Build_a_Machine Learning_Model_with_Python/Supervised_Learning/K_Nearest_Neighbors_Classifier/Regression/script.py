from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  sum_rating = 0
  for neighbor in neighbors:
    title = neighbor[1]
    sum_rating += movie_ratings[title]
    avg_rating = sum_rating / k
  
  return avg_rating

# [budget, runtime, year]
print(movie_dataset["Life of Pi"])
print(movie_ratings["Life of Pi"])

# The normalized year is larger than 1 because our training set only had movies that were released between 1927 and 2016 — Incredibles 2 was released in 2018.
unknown_movie = [0.016, 0.300, 1.022]
print(predict(
  unknown_movie,
  movie_dataset,
  movie_ratings,
  5
))

