a=0
b=1
sumof=0
while b<4000000:
	a,b=b,a+b
	print(b,end=" ")
	if b%2==0:
		sumof+=b
print("\nsum of even fibonacci numbers:",sumof)