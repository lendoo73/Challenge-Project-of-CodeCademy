class Pokemon:
  # constructor:
  def __init__(self, name, level, typeOf, maxHealth):
    self.name = name
    self.level = level
    typeOf = typeOf.lower()
    if (typeOf == "fire" or typeOf == "water" or typeOf == "grass"):
      self.type = typeOf
    else:
      self.type = "grass"
    self.maxHealth = maxHealth
    self.currentHealth = maxHealth
    self.isKnockedOut = False
    self.experience = 47
  
  # methods:
  def loseHealth(self, hit):
    self.currentHealth -= hit
    print("{name} loose {loose} HP. Remained {currentHealth} HP".format(name = self.name, loose = hit, currentHealth = self.currentHealth))
    if (self.currentHealth <= 0):
      self.isKnockedOut = True
      print("{name} is knocked out!".format(name = self.name))
    return self.currentHealth
  
  def gainHealth(self, heal):
    self.currentHealth += heal
    print("{name} under healing... ".format(name = self.name))
    if self.currentHealth > self.maxHealth:
      print("{name} completely healed to the maximum HP.".format(name = self.name))
      self.currentHealth = self.maxHealth
    print("{name} has {currentHealth} HP".format(name = self.name, healed = heal, currentHealth = self.currentHealth))
    if self.currentHealth > 0:
      if self.isKnockedOut:
        self.isKnockedOut = False
        print("You are ready to attack anyone BUT be carefull, you are also attackable!")
    return self.currentHealth

  def getAdvantage(self, typeOf):
    attackTable = {
      "fire": {
        "fire": 0.5,
        "water": 0.5,
        "grass": 2
      },
      "water": {
        "fire": 2,
        "water": 0.5,
        "grass": 0.5
      },
      "grass": {
        "fire": 0.5,
        "water": 2,
        "grass": 0.5
      }
    }
    return attackTable[self.type][typeOf]
  
  def attack(self, enemy):
    if type(enemy) != Pokemon:
      return print("Pokemon can attack only another Pokemon...")
    if (self.isKnockedOut):
      return print("{attacker} is knocked out! You have to heal before attack.".format(attacker = self.name))
    if (enemy.isKnockedOut):
      return print("{attacker} cannot attack {enemyName} because he/she is knocked out.".format(attacker = self.name, enemyName = enemy.name))
    advantage = self.getAdvantage(enemy.type)
    damage = int(self.level * advantage * 2)
    print("{attacker} attack {defender}, damage {damage} HP and collected some XP.".format(attacker = self.name, defender = enemy.name, damage = damage))
    enemy.loseHealth(damage)
    self.experience += damage
    self.increaseLevel()

  def increaseLevel(self):
    if self.experience >= 50 * self.level:
      self.level += 1
      self.experience = 0
      self.maxHealth += 5
      print("{attacker} collected enough XP to level up! New level: {level}".format(attacker = self.name, level = self.level))
  
  def getXP(self):
    print("{name} has {XP} XP.".format(name = self.name, XP = self.experience))
    return self.experience


