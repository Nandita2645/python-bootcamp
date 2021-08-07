import math
l=float(input("enter length:"))
b=float(input("enter breadth:"))
h=float(input("enter height:"))
k=l**2+b**2+h**2
vol=((b**2)*(h**2))/math.sqrt(k)
print("the volume of the tromboloid is: ",'%.3f' %vol)
r=((3/4*3.14)*vol)**(1/3)
print("the radiius of the sphere is : ",'%.3f'%r)
