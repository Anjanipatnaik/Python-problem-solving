def count(n,c=0):
    if n==0:
        return c
    else:
        n = n//10
        return count(n,c+1)
n = int(input())
print(count(n))

