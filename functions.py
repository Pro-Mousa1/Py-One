greeting = "    Hello  world"
print(greeting)

capital_greeting = greeting.upper()
print(capital_greeting)

lower_greeting = greeting.lower()
print(lower_greeting)

striped_greeting = greeting.strip()
print(striped_greeting)

number = -4
print(number)

absolute_number = abs(number)
print(absolute_number)

number_squared = pow(number, 2)
print(number_squared)

# CUSTOM / USER DEFINED FUNCTIONS
def motto():
    print("Hey, this is our motto")

motto()

def add_numbers():
    x = 20
    y = 30
    z = x + y
    print(z)

add_numbers()

def addition(x,y):
    z = x + y
    print("Hey, your answer is", z)

addition(20,40)
addition(250,750)

def interest(p,r,t):
    interest = ( p * r * t) / 100
    print(interest)

interest(2000,3,5)

# Create a function to calculate
# the bmi of any person. Use scale
# 0 ----18 ----Underweight
# 18.1 -----29 ----Normal weight
# 29.1----- 34 ----Overweight
# 34.1 and above--Obese

def bmi(w,h):
    bmi = w /pow(h, 2)
    if bmi <= 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")

bmi (70, 1.5)
