# Start by asking the number of names
number_of_names = input("How many names do you have?\n")
# Convert the received number to an integer
number_of_names = int(number_of_names)
# Direct the user to start entering the names
print("Enter the",number_of_names,"names")
# Prepare an empty list to start receiving the names
names = []
# Write a loop to receive names one by one
counter = 0
while counter < number_of_names:
    names.append(input())
    counter += 1

# Write a loop to print the received names
for elle in names:
    print(elle)
