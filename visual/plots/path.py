import matplotlib.pyplot as plt

def coords():

  print("Please provide a value for the X axis.")
  
  Xaxis = int(input())

  print("please provide a value for the Y axis.")

  Yaxis = int(input())
  
  return(Xaxis, Yaxis)

def path():

  print("Creating path...")

  xval = []

  yval = []

  for counting in range(4):

    plotdata = coords()

    xval .append(plotdata[0])
    yval .append(plotdata[1])

  return(xval, yval)

def run ():

  axvalues = path()

  plt.plot(axvalues[0], axvalues[1], 'r--o')
  
  plt.xlabel("X Axis")
  plt.ylabel("Y Axis")
  plt.show()

run()