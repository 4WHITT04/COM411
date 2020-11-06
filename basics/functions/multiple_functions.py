#first of two functions for program
def ladder_show(slats):

  for climb in range(slats):

    print("|----|")
  

  
#second function for collecting user input.
def how_many():

  print("Hey beep? how many slats are there to the top of the ladder!")
  
  print()
  
  howman = int(input())
  
  print()
  #function call for displaying ladder.
  ladder_show(howman)


#function call for user input.
how_many()



