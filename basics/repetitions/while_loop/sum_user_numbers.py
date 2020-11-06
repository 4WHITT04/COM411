#initial comment and user input
print("how many numbers will this calculation involve?")
sumamount = int(input())

#control variable 
summish = 1

#variable for sum total
sumt = 0

#while loop for repeated number input.
while (summish <= sumamount):
  print("please enter number:", summish, "of", sumamount, ".")
  
  num = int(input())
  
  sumt = sumt + num

  summish = summish +1

#displaying calculation result.
print("Alright so the combined total should be...", sumt, "am i right?")


