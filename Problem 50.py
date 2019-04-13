#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

from PrimesTo import PrimesTo
import time
start_time = time.clock()
primes=PrimesTo(1000000)
setprimes=set(primes)
cons=0
for x in range(len(primes)):
    n=0
    result=0
    for y in range(len(primes)-x):
        result=result+primes[x+y]
        n=n+1
        if result in setprimes and n>cons:
            cons=n
            long=result
        if result>1000000:
            break

print(long)
print(time.clock() - start_time, "seconds")