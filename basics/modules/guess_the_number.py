#seperate code out into function.

def guess_the_number():
  #import required Module
  import random as rand

  print ("Alright beep, give me a number for our range.")
  #create variables for user provided range.
  num1 = int(input())

  print()
  print ("Okay, now give me a larger number then that one for the other end of the range.")

  print()
  num2 = int(input())

  #create RNG variable and apply it to range.
  rond = rand.randrange(num1, num2)


  print("So i have a number between", num1, "and", num2 ,"can you guess what it is?")
  #variable for guessed num.
  guessnum = 0

  #while loop to for RNG.
  while (guessnum != rond):
    
    guessnum = int(input())
    #if and elif statements that make up RNG. 
    if (guessnum < rond):
    
      print("thats too small.")
      print("Try again?")

    elif (guessnum > rond):
    
      print("thats too big.")
      print("Try again?")

    elif (guessnum == rond):

      print("Congratulations! You got the right number!")

#function call
guess_the_number()