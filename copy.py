l= list(map(int,input("Enter the list: ").split()))
l1=[]
l.sort()
l1=l[0:3]
sum = 0
for i in l1:
    sum = sum+i
print(sum)
