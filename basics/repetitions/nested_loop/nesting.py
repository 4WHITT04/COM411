#inituial statements and user inputs.
print("Alright Bop, give me a sequence of -'s with 2 X's in it please!'")

sequ = input()

print("Alright now enter a character please!")

posi = input()

print("Calculating...")

print("")
#variables for positon on seuqence.
posi1 = -1

posi2 = -1

for position in range(0, len(sequ), 1):
  chara = sequ[position] 

  if (chara == posi):
    
    if(posi1 == -1):
      posi1 = position
    
    else:
      posi2 = position

print("")

print("Alright so the space between our markers on the sequence is", (posi2 - posi1 - 1))