#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#Create an empty list that stores infinite inputs until invalid
#Get user input as an integer

#If the user input is invalid:
#Print invalid input and the lowest number entered and stop the loop

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

    except ValueError:
        print(f"Invalid input, the lowest number is: {min(numbers)}")
        break
