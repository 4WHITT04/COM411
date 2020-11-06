#initial comment and user input
print("Hep Bop, what strange markings do you see?")

markingsee = input()
indexno = 0

print("beginining identification...")

#for loop for character indexing
for position in range (0, len(markingsee), 1):
  
  indexno +=1

  print("printing index number", indexno, ":", markingsee[position])

print()
print("Yeah! that seems right to me!")