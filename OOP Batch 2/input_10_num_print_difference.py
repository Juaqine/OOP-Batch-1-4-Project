#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

#Initialize diff to 0
#Make the first number a variable, ask the user to enter a number
#Loop 9 numbers to enter remaining 9 numbers:
#Ask user to enter a number
#Add number to diff variable
#Subtract diff from num1
#Print result

diff = 0
num1 = float(input("Enter number 1: "))

for i in range(9):
    number = float(input(f"Enter number {i+2}: "))
    diff += number

print("The difference of all numbers is:", num1 - diff)
