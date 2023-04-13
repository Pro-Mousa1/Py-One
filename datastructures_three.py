# Start bt asking for the count of numbers
numbers = input("How many numbers do you have?\n")
# Convert the number to integer
numbers = int(numbers)
# Ask the user to enter the numbers
print("Enter the",numbers,"figures")
# Prepare an empty list to receive the numbers
betting_numbers = []
# Write a loop to receive the numbers one by one
counter = 0
while counter < numbers:
    betting_numbers.append(input())
    counter += 1
# Ask the user to give you the number he/she wants to bet with
lucky_number = input("Enter the number you wish to bet with?\n")
# Check if the number exists on the list of numbers received
# Write a loop to navigate through the list as you check
for il in betting_numbers:
    if il == lucky_number:
        print("Congrats!!! You won")
        break


