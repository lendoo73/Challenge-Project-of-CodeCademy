class Trainer:
  # constructor:
  def __init__(self, name, potions):
    self.students = []
    self.name = name
    self.potions = potions
    self.currentPokemon = -1 # the Pokemon who is active currently, maybe this is the index???
  
  # methods:
  def addStudent(self, student):
    if len(self.students) < 6:
      self.students.append(student)
      print("{trainerName} just got a new student named {studentName}.".format(trainerName = self.name, studentName = student.name))
    else:
      print("Sorry, {trainerName} cannot accept another student...".format(trainerName = self.name))

  def removeStudent(self, student):
    # check if student exists:
    if student in self.students:
      self.students.remove(student)
      print("{studentName} left the {trainerName} trainer...".format(trainerName = self.name, studentName = student.name))
      if len(self.students) == 0:
        self.currentPokemon = -1
    else:
      print("{studentName} never visited {trainerName} trainer...".format(trainerName = self.name, studentName = student.name))

  # heal the active Pokemon:
  def usePotion(self):
    if self.potions > 0:
      currentPok = self.getActiveStudent()
      if currentPok:
        print("{trainerName} heals {studentName}...".format(trainerName = self.name, studentName = currentPok.name))
        currentPok.gainHealth(10)
        self.potions -= 1
    else:
      print("{trainerName} trainer run out from potions... ".format(trainerName = self.name))
    
    # choose active Pokemon from the list:
  def activateStudent(self, student):
    if student in self.students:
      if student.isKnockedOut:
        return print("{trainerName} cannot to  activate a knocked out Pokemon...".format(trainerName = self.name))
      # get the position of the student:
      self.currentPokemon = self.students.index(student)
      print("{trainerName} trainer activated {studentName} Pokemon".format(trainerName = self.name, studentName = student.name))
    else:
      print("{studentName} is not the {trainerName}'s student.".format(trainerName = self.name, studentName = student.name))

  def getActiveStudent(self):
    if self.currentPokemon > -1:
      return self.students[self.currentPokemon]
    else:
      print("{trainerName} did not choose active Pokemon...".format(trainerName = self.name))
      return False
  
  def attack(self, enemy):
    if type(enemy) == Trainer:
      print("{trainerName} attack {enemyName}".format(trainerName = self.name, enemyName = enemy.name))
      currentAttacker = self.getActiveStudent()
      if currentAttacker:
        currentDefender = enemy.getActiveStudent()
        if currentDefender:
          # attack possible:
          currentAttacker.attack(currentDefender)
    else:
      print("Trainer can attack only another trainer...")


      
