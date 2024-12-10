"""
n=4
1
121
12321
1234321
"""
n = int(input("Enter the number = "))
s = ""
for i in range(1,n+1):
    s=s+str(i)  #s="1" + "2"
    print(s+s[-2::-1])

#s = "123456"
