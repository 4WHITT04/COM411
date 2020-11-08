#initial function for tuple.
def likelihood():
  #tuple with populated values
  likelihoods = (50, 38,27, 99, 4)

  #return for tuple.
  return min(likelihoods)

#second function
def run():

  #function call
  likelihood()

  #local variable for function call.
  chance = likelihood()

  #print statement to display min value in tuple.
  print("Alright Beep, it looks like the lowest chance of us falling is... {}%" .format(chance))

#function call for run.
run()