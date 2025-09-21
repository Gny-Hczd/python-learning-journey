You can find palindrome numbers up to n and sum of them with the help of this program:


n=int(input("enter the number:"))
print(f"palindrome numbers from 1 to {n}")
sum=0
for i in range(1,n):
	if str(i)==str(i)[::-1]:
		sum+=i
		print(i,end=" ")
print("\nsum of them:",sum)

