L = list(map(int, input("Enter the list:").split()))
L.sort()
sum  = 0
l2 = []
l2 =L[-1:-4]
for i in l2:
    sum = sum +i
    print(sum)

