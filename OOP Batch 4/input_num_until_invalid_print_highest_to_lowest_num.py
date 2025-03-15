#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

#Create an empty list that stores infinite numbers entered
#Start an infinite loop that ask for user input
#Get user input as an integer

#If the user input is invalid:
#Goes through the list to sort the numbers entered in descending order
#Print invalid input and the descending order of number entered and stop the loop

numbers = []

while True:
    try:
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
        numbers.sort(reverse=True)
    except ValueError:
        print("Invalid input. The descending order of what you entered is: ", numbers)
        break
