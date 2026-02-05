num1=1
num2=2
sum=num1+num2
sumofeven=2
while sum<4*10**6:
	num1=num2
	num2=sum
	sum=num1+num2
	if num2%2==0:
		#sum of even-valued Fibonacci numbers
		sumofeven+=num2
print(sumofeven)