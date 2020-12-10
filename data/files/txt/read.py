#first function
def search (fname):
  
  print("Searching for locations...")

  #with to read from txt file
  with open(fname) as fname:
    #for loop to print txt file
    for line in fname.readlines():
      
      print("We've looked in the: {}" .format(line.strip()))
  
  print("Alright, we're done!")


#second function
def run():
  #seach function to find txt file.
  search("data/files/txt/locations.txt")


#function call.
run()

