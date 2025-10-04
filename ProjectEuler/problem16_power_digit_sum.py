num=pow(2,1000)
sumof=0
while num>0:
	sumof+=num%10
	num=num//10
print("the sum of the digits of the number 2^1000 is",sumof)