import matplotlib.pyplot as plt

def read_data(fileP):

  tempdata = []

  with open(fileP) as file:

    for line in file:
      
      tempdata.append(float(line.strip()))
    
  return tempdata

def run():

  datatemps = read_data('visual/subplots/tempdata.txt')
  
  fig, (ax1, ax2) = plt.subplots(1 , 2)

  ax1.plot(range(len(datatemps)), datatemps)
  ax2.bar(range(len(datatemps)), datatemps)
  plt.show()

run()