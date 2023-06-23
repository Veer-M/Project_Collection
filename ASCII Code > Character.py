'''
   Description: This program receives an ASCII code and displays its character
   Input: Console input ASCII code
   Output: Console output ASCII character
   Known bugs: Error if non-integer value or integer not between 0 and 127 is inputted
'''

Numb = int(input("Enter an ASCII code: "))
print(chr(Numb))

'''
Enter an ASCII code: 101
e
'''
