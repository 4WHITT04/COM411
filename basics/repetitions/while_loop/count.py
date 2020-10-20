#user will provide input
print("There are lots of live cables in the way, if they touch me i'll be fried! How many do i need to avoid?")

cabavoid = int(input())

cabavoided = 0

while (cabavoided < cabavoid):

  cabavoided = cabavoided +1
  avoidedcab = cabavoided
  print("Avoiding cable. . . ", end="")
  print(avoidedcab, "live cables avoided!")

print()
print("I have avoided all the cables!")