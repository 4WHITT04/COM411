#initial statements and user inputs.
print ("program commencing...")

print ("Hello user, please enter a valid ascii code:")

print()

#ascii code variable.
asciicode = int(input())

#if statement to convert code to character.
if (asciicode > 32 and asciicode < 126):
  print("The acii code", asciicode, "represents the:", chr(asciicode), "character.")

else:
  print ("please provide a valid ascii code that REPRESENTS A CHARACTER.")

print()

print("Character provided, terminating program.")
