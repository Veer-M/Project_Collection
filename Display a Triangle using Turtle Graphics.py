'''
   Description: This program prompts the user and plots three points for a triangle and displays it using turtle graphics
   Input: Console input three coordinate positions of a triangle
   Output: Console output visual triangle with three angles
   Known bugs: When console input is not numerical values
'''

import turtle
import math

print("Use point format: x1, y1, x2, y2, x3, y3")
a, b, c, d, e, f = eval(input("Enter three points: "))

A = math.sqrt((c-e)*(c-e)+(d-f)*(d-f))
B = math.sqrt((a-e)*(a-e)+(b-f)*(b-f))
C = math.sqrt((a-c)*(a-c)+(b-d)*(b-d))

AngA = math.degrees(math.acos((A*A-B*B-C*C)/(-2*B*C)))
AngB = math.degrees(math.acos((B*B-C*C-A*A)/(-2*A*C)))
AngC = math.degrees(math.acos((C*C-B*B-A*A)/(-2*B*A)))

AngA = round(AngA, 2)
AngB = round(AngB, 2)
AngC = round(AngC, 2)

turtle.penup()

turtle.goto(a, b)
turtle.pendown()
turtle.write("p1 (" + str(AngA) + ")")
turtle.goto(c, d)
turtle.write("p2 (" + str(AngB) + ")")
turtle.goto(e, f)
turtle.write("p3 (" + str(AngC) + ")")
turtle.goto(a, b)

turtle.done()

'''
Visual Output
'''
