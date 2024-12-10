"""
n=1234
rev=	0

n	rem=n%10	rev=rev*10+rem	n=n//10
1234	4	 0*10+4 = 4	123
123	3	4*10+3=43	12
12	2	43*10+2=432	1
1	1	432*10+1=4321	0
0==============================================

"""
n = int(input("Enter the value = "))
rev = 0
originalval = n
while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10
if originalval==rev:
    print(rev,"is a palindrome")
else:
    print(originalval,"is not a palindrome as its rev = ",rev)


