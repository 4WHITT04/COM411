# code showing elif, if, and else statements for decision making. 
print("I am doing some painting, what direction should i paint first?")
direction = input()

if (direction == "up"):
  print("Okay, i'll paint upwards!")
#first use of an elif statement
elif (direction == "left"):
  print("Okay, i'll paint to the left!")

elif (direction == "right"):
  print("Okay, i'll paint to the right!")

elif (direction == "down"):
  print("Okay, i'll paint downwards!")

else:
  print("Invalid direction!")
