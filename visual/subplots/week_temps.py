import csv
import matplotlib.pyplot as plt

#first function
def readdata ():

  #open csv file
  with open("visual/subplots/temps.csv") as csvfile:
    
    #csv file variable
    readcsv = csv.reader(csvfile)

    heading = next(readcsv)
    #dict for file data
    datcsv =  {'week1':[], 'week2':[]}

    #for loop to read file data. 
    for line in readcsv:

      datcsv['week1'].append(float(line[1].strip()))
      datcsv['week2'].append(float(line[2].strip()))

  return datcsv

def run():

  readcall = readdata()

  fig, (ax1, ax2) = plt.subplots(1, 2)

  ax1.plot(range(len(readcall['week1'])), readcall['week1'])
  ax2.plot(range(len(readcall['week2'])), readcall['week2'])
  plt.show()

run()

  