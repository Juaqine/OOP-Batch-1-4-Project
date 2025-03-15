#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

#Initialize num to 0
#Loop while num less than or equal to 0
#Check if num does not end in 0
#If true, print the number
#Increase num by 1

num = 0
while num <= 100:
  if num % 10 !=0:
    print(num)
  num+=1
