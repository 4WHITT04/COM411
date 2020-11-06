#first function
def weight_total(beep, bop):
 
  #initial weight variables

  sumtot = beep + bop

  return(sumtot) 

#second function.
def weight_mean (beep, bop):

  weimean = beep + bop / 2

  return(weimean)

#third function
def go():

  print("Hey Beep, How much do you weigh?")

  beep  = float(input())

  print("Okay cool and my weight is....")

  bop = float(input())

  print("okay now should i get the  sum or the average?")

  sumave = str(input())
  #if statement to determine sum or average.
  if (sumave == "sum"):
    
    total = weight_total(beep, bop)
    print("Our combined weight is...{:.2f}".format(total))
  
  elif (sumave == "average"):
    
    mean = weight_mean(beep,bop)
    print("The average? well that is...{:.2f}". format(mean))
  
  else:
    print("please provide a valid input.")

go()