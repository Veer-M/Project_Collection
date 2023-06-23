'''
   CIST 005A Summer 2023
   HW week 1 problem 2.14
   Description: This program finds the area of a triangle given three points
   Input: Console input of three coordinates
   Output: Console output of triangle area
   Student: Veer Mistry
   Known bugs: Error when non-numerical values are inputted and not given in the right format (a, b, c, d, e, f)
   Date: 6/22/2023
'''

Points = input("Enter three points for a triangle: ")
PointList = Points.split(",")
a, b, c, d, e, f = map(float, PointList)
AreaValue = ((1/2)*((a*d+c*f+e*b)-(b*c+d*e+f*a)))
FinalArea = str(round((abs(AreaValue)), 1))
print("The area of the triangle is " + FinalArea)

'''
Enter three points for a triangle: 8, -4, 0, 15, 16, 19
The area of the triangle is 168.0
'''