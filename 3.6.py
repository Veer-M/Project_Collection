'''
   CIST 005A Summer 2023
   HW week 1 problem 3.6
   Description: This program receives an ASCII code and displays its character
   Input: Console input ASCII code
   Output: Console output ASCII character
   Student: Veer Mistry
   Known bugs: Error if non-integer value or integer not between 0 and 127 is inputted
   Date: 6/22/2023
'''

Numb = int(input("Enter an ASCII code: "))
print(chr(Numb))

'''
Enter an ASCII code: 101
e
'''