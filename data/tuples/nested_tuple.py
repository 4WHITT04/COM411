#first function for tuples.
def steps ():

  #list of tuples.
  steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]

  #return value.
  return (steps)

#second function.
def run ():

  #function call.
  stepping = steps()

  #empty lists.
  goodsteps = []

  badsteps = []

  for step in stepping:

    if (step[1] >= 50):

      badsteps .append(step)
    
    else:

      goodsteps .append(step)

  print("alright beep, so there are {} good steps, and there are {} bad steps" .format(len(goodsteps), len(badsteps)))

run()