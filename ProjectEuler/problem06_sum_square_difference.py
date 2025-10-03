#Difference between the square of the sum and the sum of the squares of the first n numbers.
s=0
j=0
m=int(input("enter the number:"))
for i in range(1,m+1,1):
	s+=i**2
	j+=i
j=j**2
print(j-s)
