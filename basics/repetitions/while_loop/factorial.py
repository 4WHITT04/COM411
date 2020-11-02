#initial comment and user input 
print ("Hi! Bop here, i want to work out the factorial of a number so why don't you tell me a number?")
print()
factnum = int(input())

# create variables for factorial calculcation.
factcount = 0

factresult = 1
print()
#while loop to carry out factorial calculation. 
while (factcount < factnum):
  
  factcount = factcount + 1

  factresult = factresult * factcount

print("Alright so.... the factorial of", factnum, "should be:", factresult)
