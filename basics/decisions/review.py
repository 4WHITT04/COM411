#initial user input.
print("Hi! Beep here, i'm trying to write a book. how long should it be?")

longth = input()

print("okay and what genre should it be?")

genre = input()

#if statement featuring and operator.
if ((longth == "short") and (genre == "adventure")):
  print("alright so i'll write a", longth, "story in the", genre, "genre... and what colour of pen should i use?")
  
  pencolour = input()
  #if statement featuring or operator.

  if ((pencolour == "blue") or (pencolour == "red")):
    print("Okay i'll use a", pencolour, "pen!")
  
  elif ((pencolour == "green") or (pencolour == "yellow")):
    print("The", pencolour, "pen has no ink in it...")
  
  else:
    print("I don't have a", pencolour, "pen!")

else:
  print("I don't feel like writing that... sorry!")