def inputlist():
    m=int(input("enter no of tuples: "))
    list=[]
    for i in range(m):
        s1, s2=input("enter strings: ").split()
        list.append((s1, s2))
    return list
def concatenated(list):
    return ';'.join(['='.join(ele) for ele in list])
    
def main():
    list=inputlist()
    res = concatenated(list)
    print(res)
main()
