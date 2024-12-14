n = int(input("Enter a number:"))
sum =0
for i in range(len(str(n))):
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
if sum<=1:
    print("Not a prime number")
for j in range(2, int(sum**0.5)+1):
    if sum%j==0:
          print("Not a prime number")
    else:
         print("A prime number")
         break
    
    
