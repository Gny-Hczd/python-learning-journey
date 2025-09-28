def sumof(n):
	s=0
	for i in range(1,n):
		if i%3==0 or i%5==0:
			s+=i
	return s
print(f"sum of all the multiples of 3 or 5 below 1000: {sumof(1000)}")