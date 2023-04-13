x = 10
y = 20
if x < y and x == 20:
    print("TRUE")
else:
    print("FALSE")

pi = 3.142
radius = 12
area = pi * radius * radius
if area < 1000:
    print("This is a small circle")
else:
    print("This is a big circle")


principle = 2000
rate = 5
time = 3
interest = (principle * rate * time)/100
if interest < 500:
    print("The loan is affordable")
elif interest < 1500:
    print("The loan is expensive")
else:
    print("The loan is scam")


weight = 55
height = 1.55
bmi = weight / (height * height)
if bmi <= 18:
    print("Underweight")
elif bmi <= 24:
    print("Normal weight")
elif bmi <= 29:
    print("Overweight")
else:
    print("Obese")

marks = 81
if marks < 40:
    print("D")
elif marks < 50:
    print("C")
elif marks < 60:
    print("B")
else:
    print("A")

a = 10
b = 20
if a > b:
    if b > 20:
        print("TRUE")
    else:
        print("FALSE")
else:
    if a < b:
        print("SECOND TRUE")
    else:
        print("SECOND FALSE")

# Given three variables "ageOne, ageTwo ,ageThree"
# Containing integer values ,write efficient
# python statements to satisfy the following conditions
# 1. If ageOne is greater than ageTwo , proceed to check
# the following conditions on ageThree variable
# i. if ageThree is greater than 18 ,display a
# welcome message. Else ,display a goodbye message.
# 2. ageOne is less than ageTwo , proceed to check
# the following conditions on ageThree variable
# i. if ageThree is greater than 15 ,display a
# welcome message. Else ,display a goodbye message.

ageOne = 18
ageTwo = 19
ageThree = 20

if ageOne > ageTwo:
    if ageThree > 18:
        print("Welcome")
    else:
        print("Goodbye")
else:
    if ageThree > 15:
        print("Welcome")
    else:
        print("Goodbye")
