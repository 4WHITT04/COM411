#user will input information to display beeps vital statistics via string operators.

print("System: Please display unit Beeps current amount of power cells (Max. 10).")
powercells = int(input())

print("System: Please examine unit Beeps current power cell and input its current power level (Max. 10).")
powerlevel = int(input())

print("System: Please examine unit Beeps shield strength and input the data (max. 10).")
shieldstr = int(input())

#display user inputed data using strings
print("Data input complete: displaying current data logs:\n\n")

print("P.cells:", "✚ " * powercells)
print("P.level:", "✦ " * powerlevel)
print("S.strength:", "❉ " * shieldstr)