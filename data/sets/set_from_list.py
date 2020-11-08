#initial function.
def observed():
  #list for observations.
  observations = []
  
  print("alright beep, tell me what you see:")

  #for loop for user input and list appending
  for count in range(7):


    observations.append(input())
    print()
  #return command for list.
  return(observations)

#second functino.
def run():

  #function call and local variable
  sightseen = observed()

  print()

  #statement and creating of empty set.
  print("Okay beep lets count what saw...")
  set_sights = set()

  #for loop to populate set.
  for observe in sightseen:
    
    info = (observe, sightseen.count(observe))
    
    set_sights.add(info)

  #for loop to print unique user inputs and values.
  for info in set_sights:
    print()
    print("We saw: {} and {} times!" .format(info[0], info[1]))

#final function call.
run() 
