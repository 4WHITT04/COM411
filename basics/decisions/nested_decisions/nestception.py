#code to display utilization of multiple nested decisions.
print("I've lost my spare power cell! Human, which room should i check?")

room = input()
print()

#first decision with nested decision
if (room == "bedroom"):
  print("Alright, i'll check the bedroom. Any idea where i should look in there?")

  bedcheck = input()

  if (bedcheck == "under the bed"):
    print("I found some shoes, but my power cell wasn't there!")
  else:
    print("I found a lot of mess, but my power cell wasn't in it!")
#second decision with nested decision
elif (room == "in the bathroom"):
  print("Alright, i'll check the bathroom, where should i look in there?")

  bathcheck = input()

  if (bathcheck == "in the bathtub"):
    print ("I found a rubber duck, but not my power cell!")
  else:
    print("The surfaces were really wet, and i couldn't find my power cell!")
#third decision with nested decision
elif (room == "in the lab"):
  print("Alright, i'll check the lab. Where should i look in there?")
  
  labcheck = input()
  
  if (labcheck == "on the table"):
    print("There it is! i found the power cell!")
#else statement for invalid user input
else:
  print("i don't know where that is.. but i'll keep looking!")

