print("enter two numbers: ")
x=input().split()
sum=0
for i in x:
    sum=sum+int(i)
print(f"{x[0]}+{x[1]}={sum}")
