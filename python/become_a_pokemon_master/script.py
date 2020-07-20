import pokemon
import trainer
import charmander
Pokemon = pokemon.Pokemon
Trainer = trainer.Trainer
Charmander = charmander.Charmander

csaba = Pokemon("Csaba", 1, "fire", 50)
char = Charmander("Charmander", 1, "fire", 50)
andi = Pokemon("Andi", 3, "grass", 50)
robin = Pokemon("Robin", 5, "water", 50)

#csaba.attack(andi)
andi.attack(csaba)
#csaba.attack(5)
csaba.attack(andi)
char.attack(andi)
csaba.getXP()
char.getXP()
#andi.gainHealth(15)

# instantiate a trainer:
bela = Trainer("Béla", 50)
kriszta = Trainer("Kriszta", 50)
bela.addStudent(csaba)
bela.addStudent(robin)
kriszta.addStudent(andi)
bela.activateStudent(csaba)
bela.activateStudent(robin)
kriszta.activateStudent(andi)
bela.usePotion()
bela.attack(csaba)
bela.attack(kriszta)
andi.attack(csaba)
#bela.removeStudent(csaba)
#print(type(bela))
#print(type(andi))


