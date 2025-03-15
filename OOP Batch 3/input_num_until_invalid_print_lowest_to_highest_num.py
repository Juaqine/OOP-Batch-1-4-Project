#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#Create an empty list that stores infinite numbers entered
#Start an infinite loop that ask for user input
#Try to get user input as an integer

#If the user input is invalid:
#Print invalid input and the ascending order of number entered and stop the loop

numbers = []

while True:
    try:
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
        numbers.sort()
    except ValueError:
        print("Invalid input. The ascending order of what you entered is: ", numbers)
        break
