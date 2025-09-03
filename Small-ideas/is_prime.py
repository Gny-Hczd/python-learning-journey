n=int(input()) 
a=0
if n<2:
	print("sade deyil")
else:
	for i in range(2,n): 
		if n%i==0:
			a=a+1
if a==0:
			print("sadedi")
else:
			print("sade deyil")
