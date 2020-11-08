#intial function for list.

def directions():

  #list of directions.
  directions = ["Move foward", "move backwards", "turn left", "turn right"]

  return(directions)

#secondary function call
def run():
  
  #function call.
  directions()
  
  waytogo = directions()

  print(waytogo)

run()