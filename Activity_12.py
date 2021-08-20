def inputnum():
    num=int(input("enter number: "))
    return num
def cond(a,b,c):
    if a>b and a>c:
        print(f" %d is the greatest number among {a},{b} and {c}"%a)
        return a
    elif b>c:        
        print(f" %d is the greatest number among {a},{b} and {c}"%b)
        return b
    else:        
        print(f" %d is the greatest number among {a},{b} and {c}"%c)
        return c
def main():
    a=inputnum()
    b=inputnum()
    c=inputnum()
    cond(a,b,c)

main()
