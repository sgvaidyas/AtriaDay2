"""
n=4
*
**
* *
*  *
* *
**
*
no of rows = 7 = 2n-1
no of cols = 4 = n
"""
n = int(input("Enter the number = "))
for i in range(1,2*n):
    for j in range(1,n+1):
        if j==1 or i==j or i+j==2*n:
            print("*",end="")
        else:
            print(" ",end="")
    print()