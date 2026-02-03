num=1
sum=0
while num<=1000:
#Solution that calculates the sum of self powers (nⁿ) from 1 to 1000 in Python
	sum+=pow(num,num)
	num+=1
print(sum)