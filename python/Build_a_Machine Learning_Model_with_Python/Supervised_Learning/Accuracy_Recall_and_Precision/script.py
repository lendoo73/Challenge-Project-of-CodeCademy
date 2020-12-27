labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives, true_negatives, false_positives, false_negatives = [0] * 4

for i, guess in enumerate(guesses):
  label = labels[i]
  true_positives += 1 if guess == label and guess == 1 else 0
  true_negatives += 1 if guess == label and guess == 0 else 0
  false_positives += 1 if guess != label and guess == 1 else 0
  false_negatives += 1 if guess != label and guess == 0 else 0
    
accuracy = (true_positives + true_negatives) / len(guesses)
print(accuracy)

recall = true_positives / (true_positives + false_negatives)
print(recall)

precision = true_positives / (true_positives + false_positives)
print(precision)

f_1 = 2 * precision * recall / (precision + recall)
print(f_1)
