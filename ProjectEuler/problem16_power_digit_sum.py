sum=0
num=pow(2,1000)
while num>0:
	sum+=num%10
	num=num//10
#sum of digits of the number 2^1000
print(sum)