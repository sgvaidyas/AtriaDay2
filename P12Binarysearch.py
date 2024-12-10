"""
	0	1	2	3	4
a	11	22	33	44	55
n=5						sk=55
low=0	low	high	mid		if(a[mid]==sk)
high=n-1	0	4	2		sk found
	3	4	3		elif(a[mid]<sk)
	4	4	4		low=mid+1



	0	1	2	3	4
a	11	22	33	44	55
n=5						sk=66
low=0	low	high	mid		if(a[mid]==sk)
high=n-1	0	4	2		sk found
	3	4	3		elif(a[mid]<sk)
	4	4	4		low=mid+1
	5	4	low>high--not found








	0	1	2	3	4
a	11	22	33	44	55
n=5						sk=11
low=0	low	high	mid		if(a[mid]==sk)
high=n-1	0	4	2		sk found
	0	1	0		elif(a[mid]<sk)
					low=mid+1
					else
					high=mid-1


	0	1	2	3	4
a	11	22	33	44	55
n=5						sk=10
low=0	low	high	mid		if(a[mid]==sk)
high=n-1	0	4	2		sk found
	0	1	0		elif(a[mid]<sk)
	0	-1	not found		low=mid+1
					else
					high=mid-1

							0

"""

a = eval(input("Enter the list = "))
n = len(a)
a.sort()
sk = int(input("Enter the key = "))
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==sk:
        print("the key found at index= ",mid)
        break
    elif(a[mid]<sk):
        low=mid+1
    else:
        high=mid-1
else:
    print("Search key not found")