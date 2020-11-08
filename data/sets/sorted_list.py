def observed():
  #list for observations.
  observations = []
  
  print("alright beep, what did we see in the city?:")

  #for loop for user input and list appending
  for count in range(5):

    observations.append(input())
    print()
  #return command for list.
  return(observations)

def remove_observation(observations):
  
  running_status = True

  while(running_status):
    print("do you want to remove anything from that list?")
    remove = input()
  
    if (remove == "yes"):
      
      print("okay, what would you like to remove?")

      observation = input()

      observations.remove(observation)
    
    else:

      running_status = False

    return(observations)

def run():

  observations = observed()

  remove_observation(observations)

  observe_set = set()

  for observation in  observations:
    info = (observation, observations.count(observation))
  
    observe_set.add(info)

  for info in sorted(observe_set):
    print()
    
    print("okay, so we saw the {}, {} times." .format(info[0], info[1]))


run()