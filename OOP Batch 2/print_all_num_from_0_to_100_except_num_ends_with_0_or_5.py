#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#Initialize num to 0
#Loop while num less than or equal to 100
#Check if num does not end in 0 or 5
#If true, print the number
#Increase num by 1

num = 0
while num <= 100:
    if num % 10 and num % 5 != 0:
        print(num)
    num += 1
