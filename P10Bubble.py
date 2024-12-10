def bubblesort(a):
    n=len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

a=[22,11,30,10,5]
bubblesort(a)
print("the sorted array")
print(a)

"""
	0	1	2	3	4		n=5			
a	22	11	30	10	5					
										
i=0	22	11								
cmp=4	11	22	30							
			30	10				i	cmp	n=5
			10	30	5			0	4	n-1-i
				5	30			1	3	
								2	2	
i=1	11	22	10	5				3	1	
cmp=3		22	10							
		10	22	5						
			5	22						
										
i=2	11	10	5							
cmp=2	10	11	5							
		5	11							
										
										
i=3	10	5								
cmp=1	5	10								

"""