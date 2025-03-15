#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#Ask the user to input the 1st number
#Ask the user to input the 2nd number
#Identify the smaller and larger number
#Loop from the smaller number + 1 to the larger number - 1
#Print each number in the range

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("please enter the 2nd number: "))

for i in range(num1+1,num2):
    print(i)
