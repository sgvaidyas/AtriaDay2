"""
n=4
*
***
*****
*******
"""
n = int(input("Enter the number = "))
s = "*"
for i in range(1,n+1):
    print(s*(2*i-1))