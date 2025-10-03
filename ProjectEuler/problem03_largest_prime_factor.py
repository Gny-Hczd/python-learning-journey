a=600851475143
i=2
while i*i<=a:
	if a%i==0:
		largest=i
		a=a//i
	else:
		i+=1
if a>1:
	largest=a
print(largest)