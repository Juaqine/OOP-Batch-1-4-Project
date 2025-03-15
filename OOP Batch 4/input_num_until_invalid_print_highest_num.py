#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#Create an empty list that stores infinite inputs until invalid
#Get user input as an integer
#Stores the number entered on the list

#If the user input is invalid:
#The program goes through the list and check the highest number
#Print invalid input and the highest number entered and stop the loop

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print(f"Invalid input, the lowest number is: {max(numbers)}")
        break
