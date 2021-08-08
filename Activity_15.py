def inputlist():
    return input().split()
def main():
    print("enter the list: ")
    list=inputlist()
    list.sort()
    print("sort method: ",list)
    listsorted=sorted(list)
    print("sorted method: ",listsorted)
main()
