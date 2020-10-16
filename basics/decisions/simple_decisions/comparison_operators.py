#code for comparison operators to determine the size of a number. 
print("I need you to enter a number, could be any number!")
numone = int(input())

print("Now, enter a second number!")
numtwo = int(input())

#if and elif statements to compare and determine which number is smaller.
if (numone < numtwo):
  print(numone, "is smaller then", numtwo, ",therefore the first number you entered is smaller!")

elif (numone > numtwo):
  print(numone, "is bigger then", numtwo, ",therefore the second number you entered is smaller!")
#elif statement for if two of the same number are entered.
elif (numone == numtwo):
  print("These two numbers are the same! Try something else.")