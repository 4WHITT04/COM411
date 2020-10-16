#user to input three numbers.
print("Alright, i want you to give me a number! Any number will do.")
numone = int(input())

print("Cool! Now give me a second number, please.")
numtwo = int(input())

print ("Fantastic, now a third number if you'd be so kind.")
numthree = int(input())

evennum = 0

oddnum = 0

#code to determine if a number is even of odd. 
if (numone % 2 == 0):
  evennum = evennum + 1
else:
  oddnum = oddnum +1

if (numtwo % 2 == 0):
  evennum = evennum + 1
else:
  oddnum = oddnum +1

if (numthree % 2 == 0):
  evennum = evennum + 1
else:
  oddnum = oddnum +1

#program will now display results

print("Out of the numbers you gave me, {} were even and {} were odd." .format(evennum, oddnum))