"""
n=4
11
1221
123321
12344321
"""

n = int(input("Enter the number = "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="\t")
    for j in range(i,0,-1):
        print(j,end="\t")
    print()