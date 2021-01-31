class Atom:
  def __init__(self, label):
    self.label = label

  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
#salt = Molecule([sodium, chlorine])
salt = sodium + chlorine
for atom in salt.atoms:
  print(atom.label)
