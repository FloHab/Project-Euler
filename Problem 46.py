#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#odd_composite=p+2*a^2
import time
from PrimesTo import PrimesTo
start_time = time.clock()
'Define a function to check if a composite number is in accordance to Goldbach'
def goldbach_test(x):
    for a in basis:
        if a>((x/2)**(0.5)):
            return(False)
        if (x-(2*a**2)) in primes:
            return(True)
'Create list of Primes, list of composites and list of bases'
primes=PrimesTo(60000)
odd_composites=set(range(3,60001,2))
basis=set(range(1,175)) #sqrt(60000/2)
'Remove primes from odd_composites list'
for x in primes:
    try:
        odd_composites.remove(x)
    except KeyError:
        pass
'Check all numbers below 6000 if they are in accordance to Goldbach'
for x in odd_composites:
    if goldbach_test(x)==False:
        print(x)
        break
print(time.clock() - start_time, "seconds")
print('Ganz genau Nils, du siehst richtig nur:',round((time.clock()-start_time),2),' Sekunden!')

