# ----- Setting up ----- 
import random

name = "Csaba"
question = "Will I win the lottery?"
answer = ""

# -----  Generating a random number----- 
random_number = random.randint(1, 10)  # generate a random number between 1 (inclusive) and 9 (inclusive)
#print(random_number)

# ----- Control Flow ----- 
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:   # Optional Challenges
  answer = "What would you answer?"
else:
  answer = "Error"

# ----- Seeing the result -----
# question
if name != "":
  print(f"{name} asks: {question}")
else:
  print(f"Question: {question}")
 
# answer
if question != "":
  print(f"Magic 8-Ball's answer: {answer}")
else:
  print(f"The Magic 8-Ball cannot provide a fortune unless you ask it something.") 
  
