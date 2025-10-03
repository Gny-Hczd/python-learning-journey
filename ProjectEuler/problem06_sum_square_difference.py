#Difference between the square of the sum and the sum of the squares of the first n numbers.
sum_of_squares=0
square_of_sum=0
n=100
for i in range(1,n+1,1):
        sum_of_squares+=i**2
        square_of_sum+=i
square_of_sum=square_of_sum**2
print("difference:",square_of_sum-sum_of_squares)