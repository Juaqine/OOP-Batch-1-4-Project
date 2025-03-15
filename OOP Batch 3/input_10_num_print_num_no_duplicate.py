#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#Create an empty list
#Loop 10 times to get user input
#The entered numbers are stored in the list (numbers)

#Create a different list for not repeating numbers
#Check if numbers stored in both list does not repeat through looping
#If it does not repeat:
#Add it to the 2nd list (unique_num)

#Prints non repeating number

number = []

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    number.append(num)

unique_num = []
for num in number:
    if number.count(num) == 1:
        unique_num.append(num)

print("These numbers don't repeat: ", unique_num)
