def XoR(n):
    if n%4 ==1:
        return 1
    if n%4 ==2:
        return n+1
    if n%4 ==3:
        return 0
    if n%4 ==0:
        return n
l=int(input("Enter the lower limit:"))
r=int(input("Enter the upper limit:"))
a=XoR(l-1)
print(a)
b=XoR(r)
print(b)
c=a^b
print(c)
    
    
