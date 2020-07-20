import random

money = 100

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
value = [* range(2, 15)] # https://www.geeksforgeeks.org/range-to-a-list-in-python/
deck = []

#Write your game of chance functions here

def winner(bet, multiple = 1):
    bet *= multiple
    print("You win $" + str(bet) + "!")
    print("You have $" + str(money + bet) + ".")
    return bet

def looser(bet):
    print("Sorry, you loose $" + str(bet) + "...")
    print("Still remained $" + str(money - bet) + "...")
    return bet * -1

def endOfGame(guess, result, bet, multiple = 1):
    if guess == result:
        return winner(bet, multiple)
    else:
        return looser(bet)

def coinFlip(guess, bet):
    num = random.randint(1, 2)
    result = "Heads" if num == 1 else "Tails"
    print("")
    print("The coin is flipping...")
    print("Your tip: ", guess)
    print("The result is: ", result)
    return endOfGame(guess, result, bet)
    
def oddOrEven(num):
    return "odd" if num % 2 == 1 else "even"

def choHan(prediction, bet):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    added = dice1 + dice2
    result = oddOrEven(added)
    print("")
    print("Two dice rolls...")
    print("First dice:", dice1, " Second dice:", dice2)
    print("Your prediction is:", prediction)
    print("The result is:", result, "(" + str(added) + ")")
    return endOfGame(prediction, result, bet)

# create a deck:

def createDeck():
    for suit in suits:
        for val in value:
            deck.append([suit, val])

createDeck()
# print(deck)

def getRank(card):
    rank = {
        "11": "Jack",
        "12": "Queen",
        "13": "King",
        "14": "Ace"
    }
    if str(card[1]) in rank:
        return rank[str(card[1])]
    else:
        return card[1]

def pickingCard(bet):
    print("")
    print("The deck contains", len(deck), "cards.")
    if len(deck) < 2:
        print("Shuffle deck... please wait...")
        createDeck()
    human = deck.pop(random.randint(0, len(deck) - 1))
    house = deck.pop(random.randint(0, len(deck) - 1))
    print("You picked:", human[0], getRank(human))
    print("The house picked:", house[0], getRank(house))
    if human[1] > house[1]:
        return winner(bet)
    elif human[1] < house[1]:
        return looser(bet)
    else:
        print("It's tie, please try again.")
        return 0

def roulette(field, bet):
    num = random.randint(0, 37)
    result = oddOrEven(num)
    print("")
    print("The roulette wheel is spinning...")
    print("You choosed:", field)
    print("The winner field is:", result, num)
    if type(field) == int:
        return endOfGame(field, num, bet, 36)
    elif field == "odd" or field == "even":
        return endOfGame(field, result, bet)
    else:
        print("Your bet is invalid. Please try again...")
        return 0


#Call your game of chance functions here
money += coinFlip("Heads", 10)
money += choHan("odd", 10)
money += pickingCard(10)
money += roulette(10, 10)
