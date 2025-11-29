# This code finds the number that is evenly divisible by all the numbers from 1 to 20

s=1
for i in range(1,21):
	s*=i # Product of the first 20 numbers
for j in(2,3,5,7,11,13,17,19): 
	while all((s//j) % x==0 for x in range(2,21) ):
		s=s//j
		# Then we divide by prime numbers up to 20, checking each step
print(s)
# The result is 232792560