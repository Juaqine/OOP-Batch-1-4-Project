#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

#Ask the user to input the 1st number
#Ask the user to input the 2nd number
#Check if num1 is smaller than num2
#Print num1 if it's smaller
#Print num2 if not

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("Please enter the 2nd number: "))

if num1 < num2:
    print(f"The smaller number is: {num1}")
else:
    print(f"The smaller number is: {num2}")
