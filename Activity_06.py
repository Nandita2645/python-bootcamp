string=input("elements for the list: ")
list=string.split()
list2=list[0:3]
list[0]=list[-1]='0'
print("sliced list: ",list2)
list2[0]=list2[-1]='0'
print("replaced list1: ",list)
print("replaced list2: ",list2)
output
elements for the list: 2 4 9 1 7 
sliced list:  ['2', '4', '9']
replaced list1:  ['0', '4', '9', '1', '0']
replaced list2:  ['0', '4', '0']
