def inputnum():
    num=int(input())
    return num
def add(a,b):
    return a+b
def disp(a,b,c):
    print(f"{a}+{b}={c}")
def main():
    print("enter first number: ")
    a=inputnum()
    print("enter second number: ")
    b=inputnum()
    c=add(a,b)
    disp(a,b,c)

main()
