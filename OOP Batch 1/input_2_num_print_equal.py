#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#Ask the user to input the 1st number
#Ask the user to input the 2nd number
#Check if both numbers are equal
#Print "Equal" if true
#Print "Invalid" if false

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("Please enter the 2nd number: "))

if num1 == num2:
    print("Equal")
else:
    print("Invalid")
