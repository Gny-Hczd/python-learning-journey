import math
num=20
prime=[2]
prime2=[]
for i in range(3,num+1):
	s=i
	for k in range(2,i):
		if i%k!=0:
			s-=1
			if s==2:
				prime.append(i)
size=len(prime)
for i in range(0,size):
	prime2.append(prime[i]**int(math.log(20,prime[i])))
lcm=1
for i in range(0,len(prime2)):
	lcm*=prime2[i]
print("LCM of the first 20 numbers:",lcm)
	