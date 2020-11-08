#first function for indexed list
def movements():

  #list.
  path = ["Move foward", 10, "move backwards", 5, "turn left", 3, "turn right", 1]

  return(path)

#second function
def run():

  print("Okay Beep, so we should...", end ="")

  #function call.
  movements()
  
  #variable for list path.
  pathing = movements()



  print("{} for {} steps!" .format(pathing[0], pathing[1]))
  print()

  print("Okay Beep, so we should...", end ="")

  print("{} for {} steps!" .format(pathing[2], pathing[3]))
  print()

  print("Okay Beep, so we should...", end ="")

  print("{} for {} steps!" .format(pathing[4], pathing[5]))
  print()

  print("Okay Beep, so we should...", end ="")

  print("{} for {} steps!" .format(pathing[6], pathing[7]))


run()