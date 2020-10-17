#introductory code
print("Hi, Beep here! I'm going on an adventure, should i got on a long, short, scary, or safe adventure?")

storytype = input()

if ((storytype == "long") or (storytype == "safe")):
  print("I'll take the safe route through the garden!")

elif ((storytype == "scary") or (storytype == "short")):
  print("I'll go to the dark forest, its gonna be scary!")

else:
  print("I'm not sure which route i should take if you say that...")
