#first function.
print("Alright bop we need to figure out this word, whats the word?")
  
useword = input()

def boxshow(useword):

  print(" ---"+ "-" * len(useword) +"---")
  print("|      " + " " * len(useword) +"|")
  print("|   "+ useword +"   |")
  print("|      " + " " * len(useword) +"|")
  print(" ---"+ "-" * len(useword) +"---")

#second function
def low_case(useword):
  
  print (useword.lower())

#third function
def up_case(useword):
  
  print (useword.upper())

#fourth function
def reverse(useword):
  
  worduse = str()

  for letter in(reversed(useword)):
    worduse += letter
  
  print(f"Okay so the word if we flip it says... {worduse}")

#fifth function
def repeating(useword):

  print("Okay, how many times do we want to repeat the word?")

  wordrep = int(input())

  print((useword + "\n") * wordrep)

#sixth function.
def prog_start():

  print("Tell me what we should do?")
  print()
  print("1: Put the word in a box!")
  print("2: Put the word in lower case!")
  print("3: Put the word in upper case")
  print("4: Reverse the word like its in a mirror!")
  print("5: repeat the word a bunch of times!")

  choice = str(input())

  if (choice == "1"):
    
    boxshow(useword)
  
  elif (choice == "2"):

    low_case(useword)
  
  elif (choice == "3"):

    up_case(useword)

  elif (choice == "4"):

    reverse(useword)
  
  elif (choice == "5"):
    
    repeating(useword)

  else:

    print ("i'm sorry beep, i can't let you do that.")

  

prog_start()



  



