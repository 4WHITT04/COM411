#user is to provide beep with information
print("What is your designation, human?")
designation = input()

print("how many years have you been alive?")
years = int(input())

print("what is your height in meters to two decimal places?")
height = float(input())

print("What is your weight in kilograms, rounded to the nearest whole number?")
weight = int(input())

#beep will calculate the users information and display it
BMI = weight/height ** 2

print(designation, ", you are", years, " years old and have a body mass index of:", BMI)