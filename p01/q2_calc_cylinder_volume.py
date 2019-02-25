r = float(input("Enter radius of base of cylinder(cm)"))
h = float(input("Enter height of cylinder(cm)"))
from math import pi
a = pi * r * r
print("Base area:" + str("{0:.2f}".format(a)) + " cubic meters")
v = h * a
print("Volume of cylinder:" + str("{0:.2f}".format(v)) + " cubic centimeters")
