num=1
factorial=1
while num<100:
	num=num+1
	factorial*=num #100!
sum=0
while factorial>0:
	#sum of the digits in the number 100!
	sum+=factorial%10
	factorial=factorial//10
print(sum)