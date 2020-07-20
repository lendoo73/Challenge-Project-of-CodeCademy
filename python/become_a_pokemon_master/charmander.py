import pokemon
Pokemon = pokemon.Pokemon

class Charmander(Pokemon):
  # constructor:
  def __init__(self, name, level, typeOf, maxHealth):
    super().__init__(name, level, typeOf, maxHealth)
  
  # overrided method:
  def increaseLevel(self):
    if self.experience >= 55 * self.level:
      self.level += 1
      self.experience = 0
      self.maxHealth += 10
      print("{attacker} collected enough XP to level up! New level: {level}".format(attacker = self.name, level = self.level))
