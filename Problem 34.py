#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
from math import factorial
for x in range(3,100000):
    z=0
    for y in str(x):
        z=z+(factorial(int(y)))
    if z==x:
        print(x)