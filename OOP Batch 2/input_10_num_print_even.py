#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#Initialize even_count to 0
#Loop 10 times to get user input
#Ask the user to enter a number
#Check if the number is even by: number divided by 2 == 0
#If true, increase odd_count by 1
#Print the total count of even numbers

even_count = 0

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    if number % 2 == 0:  
        even_count += 1

print("Total even numbers:", even_count)
