# Loops
# WHILE LOOP
x = 0
while x <= 5:
    print(x)
    x += 1

f = 80
while f <= 85:
    print(f)
    f += 1

h = 100
while h >= 95:
    print(h)
    h -= 1

# Write a loop to print all even numbers
# from 0-100

even_counter = 1
while even_counter <= 100:
    if (even_counter%2) == 0:
        print(even_counter)
    even_counter += 1

# FOR LOOP
my_numbers = range(0,11)
for petite in my_numbers:
    print(petite)
