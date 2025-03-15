#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#Initialize odd_count to 0
#Loop 10 times to get user input
#Ask the user to enter a number
#Check if the number is odd by: number divided by 2 == 1
#If true, increase odd_count by 1
#Print the total count of odd numbers

odd_count = 0

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    if number % 2 == 1:
        odd_count += 1
print("Total odd  numbers:", odd_count)
