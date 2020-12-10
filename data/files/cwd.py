#import.
import os

#first function.
def cwd():
  #path retreival. 
  
  getpath = os.getcwd()

  #print statement for working directory.
  print("The current working directory is:{}" .format({getpath}))

  print()

  print("The contents of this directory is:")
  #forloop for file contents
  for fcontents in os.listdir(getpath):

    print(fcontents)

#second functinom. 
def run ():
  
  print("Running proccess: Locate Working directory...")
  
  print()
  #function call for cwd.
  cwd()

#function call for run.
run()
