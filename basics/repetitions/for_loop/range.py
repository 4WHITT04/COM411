print("Wow! it's really dark in here, what setting should we set our brightness too bop?")
#userinput and control variable. 

lightlevel = int(input())

print("Okay... adjusting brightness...")
lighter = 1
#for loop for range.
for count in range(0, lightlevel, 2):
 
  lighting = ("**"*lighter)

  print("Beeps brightness level:", lighting)

  print("Bops brightness level", lighting)
  lighter +=1

  
#end statements
print("")
print("there, now we can see!!")