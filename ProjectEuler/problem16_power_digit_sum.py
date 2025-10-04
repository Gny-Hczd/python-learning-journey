num=pow(2,1000)
total=0
while num>0:
	total+=num%10
	num=num//10
print("the sum of the digits of the number 2^1000 is",total)