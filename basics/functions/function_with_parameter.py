#starting primary function
def escape_by(plan):

  #if, elif, and else statements to decide secondary function.
  if (plan == "go over"):
    
    print("No Beep! the boulders too big to jump over!")

  elif (plan == "go around"):
    
    print("No Beep! The boulders going to fast, we'll be crushed if we go around.")
  
  elif (plan == "go in"):
    
    print("You're right, we've got to go further into the cave, run!")

  else:
    
    print("Beep you've got to come up with a plan!")

#function calls
escape_by("go over")
escape_by("go around")
escape_by("go in")
