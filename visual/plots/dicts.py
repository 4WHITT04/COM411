import matplotlib.pyplot as plt
import random as rnd

def data():

  paths = {}

  print ("Please select an option from the following characters: :\n, -- \n, -")
  
  linelook = input()

  print ("now select a colour would you like red (r), blue (b), or green (g)?")

  linecol = input()


  print ("Finally, what kind of marker should be used? circle (o), square (s), or trianlge (^)")

  linemark = input()

  paths['linelook'] = linelook
  paths['linecol'] = linecol
  paths['linemark'] = linemark

  return paths

def generate ():

  print("How many lines should be displayed?")
  
  lineno = int(input())

  for counter in range(lineno):

    linevalue = data()

    xaxis = [0, rnd.randrange (1, 10)]
    
    yaxis = [0, rnd.randrange (1, 10)]

    format = f"{linevalue['linecol']}{linevalue['linelook']}{linevalue['linemark']}" 
    
    plt.plot(xaxis, yaxis, format)
  
 

def run():
  
  print("running program.....")
  
  generate()
  plt.show()
  print("Process complete.")


run()