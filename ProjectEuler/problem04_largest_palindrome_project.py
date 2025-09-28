palindrome=[]
for a in range(100,1000):
        for b in range(100,1000):
                c=a*b
                if str(c)==str(c)[::-1]:
                        palindrome.append(c)
print(max(palindrome))