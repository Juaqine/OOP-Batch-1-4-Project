#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

#Ask the user to input the 1st number
#Ask the user to input the 2nd number
#Check if both numbers are not equal
#Print "Not Equal" if true
#Print "Invalid" if false

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("Please enter the 2nd number: "))

if num1 != num2:
    print("Not Equal")
else:
    print("Invalid")
