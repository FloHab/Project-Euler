#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from PrimesTo import PrimesTo
import time
start_time = time.clock()
for x in range(1,1000000):
    if sorted(str(x))==sorted(str(2*x)) and sorted(str(x))==sorted(str(3*x)) and sorted(str(x))==sorted(str(4*x)) and sorted(str(x))==sorted(str(5*x)) and sorted(str(x))==sorted(str(6*x)):
        print(x)
        break
print(time.clock() - start_time, "seconds")