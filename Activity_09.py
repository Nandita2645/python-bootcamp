import math
l=float(input("enter length:"))
b=float(input("enter breadth:"))
h=float(input("enter height:"))
k=float(input("enter value:"))
k=l**2+b**2+h**2
vol=((b**2)*(h**2))/math.sqrt(k)
print("the volume of the tromboloid is: ",'%.3f' %vol)
r=((3/4*3.14)*vol)**(1/3)
print("the radiius of the sphere is : ",'%.3f'%r)
Output
enter length:6
enter breadth:3
enter height:7
enter value:9
the volume of the tromboloid is:  45.486
the radiius of the sphere is :  4.749
