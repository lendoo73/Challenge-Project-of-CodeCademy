def prob_a_or_b(a, b, all_possible_outcomes):
  # probability of event a
  prob_a = len(a)/len(all_possible_outcomes)
	
	# probability of event b
  prob_b = len(b)/len(all_possible_outcomes)
	
	# intersection of events a and b
  inter = a.intersection(b)
	
	# probability of intersection of events a and b
  prob_inter = len(inter)/len(all_possible_outcomes)
	
	# add return statement here: P(A or B)
  p_a_or_b = prob_a + prob_b - prob_inter
  return p_a_or_b

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here first
print("Bonus: P(A) + P(B) - P(A and B)\n")
print("Bonus: 0.5 + 0.5 - 0 = 1\n")
print(prob_a_or_b(evens, odds, all_possible_rolls))


# rolling a die once and getting an odd number or a number greater than 2
odds = {1, 3, 5}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here second
print("Bonus: P(A) + P(B) - P(A and B)\n")
print("Bonus: 3/6 + 4/6 - 2/6 = 5/6 = 0.83\n")
print(prob_a_or_b(odds, greater_than_two, all_possible_rolls))

# selecting a diamond card or a face card from a standard deck of cards
diamond_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond'}
face_cards = {'jack_diamond', 'jack_spade', 'jack_heart', 'jack_club', 'queen_diamond', 'queen_spade', 'queen_heart', 'queen_club', 'king_diamond', 'king_spade', 'king_heart', 'king_club'}
# all cards in a deck representing the entire sample space
all_possible_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond', 'ace_heart', '2_heart', '3_heart', '4_heart', '5_heart', '6_heart', '7_heart', '8_heart', '9_heart', '10_heart', 'jack_heart', 'queen_heart', 'king_heart', 'ace_spade', '2_spade', '3_spade', '4_spade', '5_spade', '6_spade', '7_spade', '8_spade', '9_spade', '10_spade', 'jack_spade', 'queen_spade', 'king_spade', 'ace_club', '2_club', '3_club', '4_club', '5_club', '6_club', '7_club', '8_club', '9_club', '10_club', 'jack_club', 'queen_club', 'king_club'}

# call function here third
print("Bonus: P(A) + P(B) - P(A and B)\n")
print(f"Bonus: {len(diamond_cards) / len(all_possible_cards) + len(face_cards) / len(all_possible_cards) - len(diamond_cards.intersection(face_cards)) / len(all_possible_cards)}\n")
print(prob_a_or_b(diamond_cards, face_cards, all_possible_cards))
