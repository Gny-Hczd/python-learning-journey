num=1000
sum=0
while num>0:
	num-=1
	if num%3==0 or num%5==0:
		sum+=num
print(sum)