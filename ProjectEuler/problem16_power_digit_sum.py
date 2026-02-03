sum=0
num=pow(2,1000)
while num>0:
	sum+=num%10
	num=num//10
print(sum) #sum of digits of 2^1000