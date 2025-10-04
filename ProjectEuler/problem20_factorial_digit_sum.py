number=100
total=0
factorial=1
while number>0:
	factorial*=number
	number-=1
while factorial>0:
	total+=factorial%10
	factorial//=10
print(total)