class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  
  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers

    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski", "Béla"])

print(len(d_and_p))
print("Béla" in d_and_p.lawyers)
