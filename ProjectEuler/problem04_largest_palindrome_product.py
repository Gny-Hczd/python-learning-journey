maxium=100*100
for a in range(100,1000):
	for b in range(100,1000):
		if str(a*b)==str(a*b)[::-1]:
			if maxium<a*b:
				maxium=a*b
print(maxium) #largest palindrome made from the product of two-digit numbers
		