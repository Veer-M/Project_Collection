'''
   Description: This program reads a Celsius degree and converts it to Fahrenheit
   Input: Console input of a Celsius Value
   Output: Console output of temperature value converted to Fahrenheit
   Known bugs: Error message when enter a non-numerical value
'''

Celsius = float(input("Enter a degree in Celsius: "))
Fahrenheit = (9/5)*Celsius+32
print(str(Celsius) + " Celsius is " + str(Fahrenheit) + " Fahrenheit")

'''
Enter a degree in Celsius: 43
43.0 Celsius is 109.4 Fahrenheit
'''
