class SortedList(list):
  def __init__(self, lst):
    super().__init__(lst)
    self.sort()

  def append(self, value):
    super().append(value)
    self.sort()

myList = SortedList([4, 1, 5])
print(myList)

class MyDict(dict):
  def get(self, key, alt = ""):
      if super().get(key) == None:
        if alt == "":
          return "Error: key ({key}) not found.".format(key = key)
        else:
          return alt
      else: 
        return self[key]

  def keyOfValue(self, value):
    for key in self:
      print("key: ", key)
      if  self[key] == value:
        return key
    return "Error: value ({value}) not found.".format(value = value)

newDict = MyDict({
  "andi": "nice",
  "kriszta": "cute"
})

print(newDict)
print(newDict.get("béla"))
print(newDict.get("béla", "jani"))
print(newDict.keyOfValue("cute"))
print(newDict.keyOfValue("ronda"))
