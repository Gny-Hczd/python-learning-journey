#This code finds the number that is evenly divisible by all the numbers from 1 to 20

import math
print(f"The smallest number evenly divisible by 1 to 20 is: {math.lcm(*range(1,20+1))}")

#The result of it is 232792560