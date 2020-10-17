#code to display nested decisions with user input.

print("i just bought a new book! Which cover type does it have?")

covertype = input()


if (covertype == "soft"):
  print("Ah, a soft cover... and is it perfect bound?")
  
  bound = input()
  if (bound == "yes"):
    print("Ah, Soft cover, perfect bound books seem to be really popular. I should buy more of them!")
  
  else:
    print("Ah i see... i did think this book was shorter then the others. Must be sitch or spiral bound.")

elif (covertype == "hard"):
  print("Ah, its a hard cover book. No wonder it was so expensive!")

else:
  print("i don't think thats a cover type for books...")