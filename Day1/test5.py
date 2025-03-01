#from constant import *
# import constant
# print("Value of PI is :",constant.PI)
# Tried saving Constants in a different class and importing which looks like a problem - Inheritance
#import constant.*
#USING MATH
import math
import constant



print(math.pi)
def sqrtPI(PI):
    print(math.sqrt(PI))

def Surfaceareaofsphere(r):
    sfasphere = 4*constant.PI*math.pow(r,2)
    print(f"Surface Area of Sphere is : {sfasphere}")

def volumeofsphere(r):
    vlsphere= (4/3)*constant.PI*math.pow(r,3)
    print(f"Volume of Sphere is : {vlsphere}")
    
sqrtPI(constant.PI)
print('Enter the Radius of the Sphere')
radius = float(input())
Surfaceareaofsphere(radius)
volumeofsphere(radius)
