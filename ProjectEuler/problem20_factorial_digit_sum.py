number=100
sumof=0
factorial=1
while number>0:
	factorial*=number
	number-=1
while factorial>0:
	sumof+=factorial%10
	factorial//=10
print(sumof)