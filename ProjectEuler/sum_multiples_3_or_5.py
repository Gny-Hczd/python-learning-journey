def sumof(n):
        i=0
        s=0
        while i<n:
                if i%3==0 or i%5==0:
                        s+=i
                i+=1
        return s
print(f"sum of multiples of 3 and 5 below 1000:{sumof(1000)}") 
