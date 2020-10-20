#user will provide input. 
print("I need to give my new friend-bot some power! How many bars of power should i give them?")

chargenumber = int(input())

#set control variable to 0.
barcharge = 0

print()

#while Loop.
while (barcharge < chargenumber):

  barcharge = barcharge +1

  print("Giving power:", "█ " * barcharge)
  print()


"Charging complete! Hello new friend!"