#The sum of squares of the first 100 natural numbers is
sum1=sum([i**2 for i in range(1,101)])
#The square of the sum of the first 100 natural numbers is
square1=pow(sum([i for i in range(1,101)]),2)
#difference between the sum of squares of the first 100 natural numbers and the square of the sum of the first 100 natural numbers is
diff=square1-sum1
print(diff)


#answer is 25164150