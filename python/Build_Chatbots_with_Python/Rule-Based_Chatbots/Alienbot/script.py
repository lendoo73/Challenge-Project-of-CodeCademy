# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here?\n> ",
        "Are there many humans like you?\n> ",
        "What do you consume for sustenance?\n> ",
        "Is there intelligent life on this planet?\n> ",
        "Does Earth have a leader?\n> ",
        "What planets have you visited?\n> ",
        "What technology do you have on this planet?\n> "
    )

  def __init__(self):
    self.alienbabble = {
      'describe_planet_intent': r".*\s*your (planet|home).*",
      'answer_why_intent': r".*why.*you.*",
      'cubed_intent': r".*cube.* (\d+)",
      "where_spacecraft_intent": r".*where.*(craft|ship)"
    }

  # Define .greet() below:
  def greet(self):
    self.name = input("Hello Earthling, what's your name?\n> ")
    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet?\n> ")
    if will_help in self.negative_responses:
      # user don't wants to chat
      return print("Ok, have a nice Earth day!")

    # the user is interested in chatting:
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    if reply in self.exit_commands:
      print("Ok, have a nice Earth day!")
      return True

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))
  
  # Define .match_reply() below:
  def match_reply(self, reply):
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply.lower())
      if found_match and intent == "describe_planet_intent":
        return self.describe_planet_intent()
      elif found_match and intent == "answer_why_intent":
        return self.answer_why_intent()
      elif found_match and intent == "cubed_intent":
        return self.cubed_intent(found_match.groups()[0])
      elif found_match and intent == "where_spacecraft_intent":
        return self.where_spacecraft_intent()
      
    return self.no_match_intent()
      
  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = (
      "My planet is a utopia of diverse organisms and species.\n> ",
      "I am from Opidipus, the capital of the Wayward Galaxies.\n> "
    )
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = (
      "I come in peace.\n> ",
      "I am here to collect data on your planet and its inhabitants.\n> ",
      "I heard the coffee is good.\n> "
    )
    return random.choice(responses)
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    return f"The cube of {number} is {int(number) ** 3}. Isn't that cool?\n> "

  def where_spacecraft_intent(self):
    responses = (
      "My spaceship is invisible for humans.\n> ",
      "My spaceship is in Area 51. They just improved.\n> ",
      "My spaceship is behind the moon.\n> ",
      "Where I came from, there is no need for a spaceship there.\n> "
    )
    return random.choice(responses)

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = (
      "Please tell me more.\n> ",
      "Tell me more!\n> ",
      "Why do you say that?\n> ",
      "I see. Can you elaborate?\n> ",
      "Interesting. Can you tell me more?\n> ",
      "I see. How do you think?\n> ",
      "Why?\n> ",
      "How do you think I feel when you say that?\n> "
    )
    return random.choice(responses)

# Create an instance of AlienBot below:
my_bot = AlienBot()
my_bot.greet()
