N = int(input("Enter no. of candidates :"))
vote = list(map(int, input("Enter the votes:").split()))
age= list(map(int,input("Enter the ages:").split()))
c=[0]*max(vote)
for i in range(N):
    if age[i]>=18:
        c[vote[i]-1]+=1
m=max(c)
print(c.index(m)+1)
