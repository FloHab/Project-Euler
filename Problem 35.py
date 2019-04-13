#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
import time
start_time = time.clock()
from PrimesTo import PrimesTo
from PrimesTo import rotate
primes=PrimesTo(1000000)
rot_primes=[]
for x in primes:
    for y in range(len(str(x))):
        z=int(rotate(str(x),y))
        if z in primes:
            primes[x]=primes[x]+1
for x in primes:
    if len(str(x))==primes[x]:
        rot_primes.append(x)
print(len(rot_primes))
print(time.clock() - start_time, "seconds")