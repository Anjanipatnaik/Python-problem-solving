def arm(n,a =0):
    if n == 0:
        return a
    else:
        d = n%10
        a+=d**len(str(n))
        print(a)
        n = n//10
        return arm(n,a)
n = int(input("Enter the number:"))
print(arm(n))
