"""
n=4
11
1221
123321
12344321
"""
n = int(input("Enter the number = "))
s = ""
for i in range(1,n+1):
    s=s+str(i)  #s="1" + "2"
    print(s+s[::-1])

#s = "123456"
