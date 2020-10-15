#code for program featuring previously learned input and output concepts.

#user will indicate what should go in the box.
print("what character would you like to put in the box?")
chara = input()

#user will indicate how long the box will be.
print("how long will the box be? Please use whole numbers (max. 10).")
long = int(input())
print()
#box will display as ascii art.

print("#" * long)
print("#\t" + chara + "\t #")
print("#" * long)

print()