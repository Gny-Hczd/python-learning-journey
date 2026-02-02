#100!
fac=1
i=1
while i<=100:
	fac*=i
	i+=1
sum=0
#The sum of the digits in the number 100!
while fac>1:
	sum=sum+fac%10
	fac=fac//10
print(sum)