'''
   Description: This program reads an integer, and adds all the digits in the integer.
   Input: Console input of an integer between 0 and 1000
   Output: Console output of the sum of the integer digits
   Known bugs: Error when non-integer value is inputted
'''

Numb = int(input("Enter a number between 0 and 1000: "))

Digit1 = (Numb % 10)
Digit2 = ((Numb//10) % 10)
Digit3 = ((Numb//10//10) % 10)
Digit4 = (Numb//10//10//10 % 10)

print("The sum of the digits is " + str(Digit1 + Digit2 + Digit3 + Digit4))

'''
Enter a number between 0 and 1000: 869
The sum of the digits is 23
'''
