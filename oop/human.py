class human: 

  MAXENRG = 100

  def __init__(self, name="Human", age = 0):
    
    self.name = name
    self.age = age
    self.energy = human.MAXENRG

  def display(self):

    print("{}, is, {} years old with a current energy level of {}" .format(self.name, self.age, self.energy))

  def __repr__(self):

    return 'human (name = {}, age = {}, energy = {}' .format(self.name, self.age, self.energy)

  def __str__(self): 

    return 'Hello there, my name is {}, i am {} years old, and my energy levels are at {} percent.' .format(self.name, self.age, self.energy)

if (__name__ == "__main__"):

  Human = human()
  Human.display() 