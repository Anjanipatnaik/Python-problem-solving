a,b =map(int,input("Enter the 2 values:").split())
n =5
for i in range(1,n):
    a*=3
    b*=2
    if a<=b:
        print("stop")
    else:
        print(i)
        break
