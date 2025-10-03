palindrom=[]
for a in range(100,1000):
	for b in range(100,1000):
		c=a*b
		if str(c)==str(c)[::-1]:
			print(a," ",b)
			palindrom.append(c)
print(max(palindrom))
