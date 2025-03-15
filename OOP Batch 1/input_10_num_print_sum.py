#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Initialize total to 0
#Loop 10 times to get user input
#Ask the user to enter a number 10 times
#Add the number to the total
#Print the sum of all numbers

total = 0

for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    total += number 

print("The sum of all numbers is:", total)
