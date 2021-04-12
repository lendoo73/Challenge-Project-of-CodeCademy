def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

class Loot:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value

  def __repr__(self):
    return "\n{0}: \n\tweighs {1},\n\tvalued at {2}".format(self.name, self.weight, self.value)
