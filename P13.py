n=int(input("Enter n = "))
i=n
for j in range(1,n//2+1):
    print(i,j,end=" ")
    i-=1
else:
    if(n%2==1):
        print(i)