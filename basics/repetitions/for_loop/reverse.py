#initial statement and user input
print("Hey Bop, what phrase do you see?\n")

phrord = input()

print("\nlets give that a flip shall we!")

print()

#start of statment to show flipped word
print("The phrase appears to say... ", end="")

#for loop for flipping word.

for position in range(len(phrord) - 1, -1, -1):
  
  print(phrord[position], end="")

print("")
print("")
print("Does that seem right?")