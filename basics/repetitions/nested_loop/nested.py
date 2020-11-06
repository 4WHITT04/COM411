#initial statement and user input.
print("Hey Bop, how many rows should i have?")

rowno = int(input())

print("Cool! and how many collumns should i have?")

colno = int(input())

print("printing Grid!")
print()
#nested loop for grid.

for row in range(0, rowno, 1):
  for column in range (0, colno, 1):
    print("[x] ", end="")
  print()

print("there we go! Grid complete")