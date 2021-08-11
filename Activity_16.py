def inputlist():
    return input().split()
def main():
    print("enter the list: ")
    list=inputlist()
    res = [tuple(map(str, sub.split(', '))) for sub in list]
    print(res)
main()
