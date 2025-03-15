#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#Create an empty list
#Loop 10 times to get user input
#The entered numbers are stored in the list (numbers)

#Create a different list for repeating numbers
#Check if numbers stored in both list does not repeat through looping
#If it does repeat:
#Add it to the 2nd list (unique_num)

#Prints repeating number

number = []

for i in range(10):
    num = float(input(f"Enter a number {i+1}: "))
    number.append(num)

duplicates = []
for num in set(number):
    if number.count(num) > 1:
        duplicates.append(num)

print("These numbers appear more than once: ", duplicates)
