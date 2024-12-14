n = int(input())
unsolved = 0
police_recruit = 0
event = list(map(int,input().split()))
for i in event:
    if i ==-1:
        if police_recruit >0:
            police_recruit-=1
        else:
            unsolved+=1
    else:
        police_recruit+=i
print(unsolved)
