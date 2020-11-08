#intial function for list.

def directions():

  #list of directions.
  directions = ["Move foward", "move backwards", "turn left", "turn right"]

  return(directions)

#second function for Menu

def menu():

  print("Hey beep, which direction should we go?")

  waytogo = directions()
  #for loop for menu.
  for index in range (len(waytogo)):

    print("{}: {}" .format(index, waytogo[index]))
  
def run():

  menu()

run()