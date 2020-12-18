class robot: 

  MAXENRG = 100

  def __init__(self, name="Robot", age = 0, energy = 0):
    
    self.name = name
    self.age = age
    self.energy = robot.MAXENRG

  def display(self):
    print("{}, is, {} years old with a current energy level of {}" .format(self.name, self.age, self.energy))

  
  def __repr__(self):

    return 'robot (name = {}, age = {}, energy = {}' .format(self.name, self.age, self.energy)

  def __str__(self): 

    return 'Greeting life form, my designation is {}, i am {} cycles old, and my energy levels are at {} percent.' .format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  Robot = robot()
  Robot.display() 