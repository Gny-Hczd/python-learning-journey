num=10**4-1 # 10000
sumof=0 
while num<=99999:
	sum=0
	num+=1
	num2=num
	for i in range(5):
		sum+=(num2%10)**5 
		num2=num2//10
	if sum==num:
		sumof+=num # num - numbers that can be written as the sum of fifth powers of their digit (amstrong nums)	
print(sumof) # sum of all numbers that can be written as the sum of fifth powers of their digits
