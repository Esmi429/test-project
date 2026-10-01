#Take three inputs from a user, separately. Print the largest of the numbers.
##    Hint: Determine what type of data is taken in as input.
num1=60
num2=40
num3=90
num1=input("Enter the first number")
num2=input("Enter the second number")
num3=input("Enter the third number")

#change into integer
num1=int(input("Enter the first number"))
num2=int(input("Enter the first number"))
num3=int(input("Enter the first number"))
largest=max(num1,num2,num3)

if num1>num2 and num1>num3:
    print('First number is the largest')
elif num2>num1 and num2>num3:
    print('The second number is the largest')
else:
    print('The third number is the largest')

#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

