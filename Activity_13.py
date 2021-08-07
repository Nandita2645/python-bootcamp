def inputnum():
    num=int(input("enter number: "))
    return num
def prime(num,x):
    if num>1:
        for x in range(2,int(num/2)+1):
            if (num%x)==0:
                print("%d is not a prime number"%num)
                break
        else:
             print("%d is a prime number"%num)
def main():
    num1=inputnum()
    x=0
    prime(num1,x)
main()
