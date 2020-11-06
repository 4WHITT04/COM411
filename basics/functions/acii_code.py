#initial statements and user inputs.
print ("program commencing...")

print ("Hello user, please enter a single Standard use character:")

print()

strdchara = input()

print()

if (len(strdchara) == 1):
  print("The character", strdchara, "carries the acii code of:", ord(strdchara))

else:
  print("Invalid input, please input a SINGLE character.")

print("")

print("Ascii code provided, program terminating.")