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

  way = int(input())

  return(waytogo[way])

def run():

  route = []

  print("i need to figure the route out...")

  for count in range (5):

    waylog = menu()

    route.append(waylog)

  print("This is how we escape! We: {}" .format(route))

run()
