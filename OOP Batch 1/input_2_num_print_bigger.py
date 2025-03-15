#Prog01: Create a program that ask the user to input 2 numbers. Print the bigger number.

#Ask the user to input the 1st number
#Ask the user to input the 2nd number
#Check if num1 is greater than num2
#Print num1 if it's greater
#Print num2 if not

num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))

if num1 > num2:
    print(f"The bigger number is: {num1}")
else:
    print(f"The bigger number is: {num2}")
