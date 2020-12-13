import matplotlib.pyplot as plt

def display (x, y):

  plt.plot(x, y)
  plt.show()


def run ():

  print("displaying data in readable format....")

  xVal = [1, 2, 3, 4, 5]

  yVal = [1, 4, 9, 16, 25]

  display(xVal, yVal)



run()