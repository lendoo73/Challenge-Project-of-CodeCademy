class Circle:
  # ----- Variables -----
  pi = 3.14
  
  # ----- Magic methods (dunder methods) -----
  # constructor (init method):
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  # String Representation
  def __repr__(self):
    return "Circle with radius {radius}".format(radius = self.radius)
  
  # ----- Methods -----
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


