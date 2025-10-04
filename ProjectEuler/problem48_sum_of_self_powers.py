a=1
total=0
while a<=1000:
	total+=pow(a,a)
	a+=1
print(f"The last ten digits of the series 1^1+2^2+3^3+...+999^999+1000^1000 are: {total%10**10}")
