
L = list(map(int, input("Enter the list:").split()))
n=len(L)
l2=[]
for i in range(1,n,1):
    if i%2==0:
        l2.append(i)
print(l2)
        
