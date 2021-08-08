import math
def inputnum():
    num=float(input())
    return num
def valuek(l,b,h):
    k=l**2+b**2+h**2
    return k
def volume(b,h,k):
    vol=((b**2)*(h**2))/math.sqrt(k)
    return vol
def radius(vol):
    r=((3/4*3.14)*vol)**(1/3)
    return r
def main():
    print("enter the length: ")
    len=inputnum()
    print("enter the breadth: ")
    bre=inputnum()
    print("enter the height: ")
    hei=inputnum()
    k=valuek(len,bre,hei)
    vol=volume(bre,hei,k)
    print("the volume of the tromboloid is: ",'%.3f' %vol)
    r=radius(vol)
    print("the radius of the sphere is : ",'%.3f'%r)
main()
