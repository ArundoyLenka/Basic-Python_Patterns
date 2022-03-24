#basic python program to find the factorial of a number using while loop

num = int(input("Enter a whole number: "))

i = 1               #here we have intialised a counter which will start from 1 and increase after every while

result = 1          #here we have assigned a variable 'result' the constant 1, 

while i <= num:             #in while loop it basically means, if i is less than equal to num
    result = result * i     #then we will have result multiply with i and i increases after the multiplication
    i += 1

print("The factorial of the number you entered is: {}".format(result))    