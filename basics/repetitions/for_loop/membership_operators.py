#initial statement and user input
print("Hey Bop, what phrase do you see?\n")

phrord = input()

print("\nlets give that a flip shall we!")

print()

#start of statment to show flipped word
print("The phrase appears to say... ", end="")

#reversed statement
reversed = ""

#for loop
for letter in phrord:

  reversed = letter + reversed

#closing print statement
print(reversed)