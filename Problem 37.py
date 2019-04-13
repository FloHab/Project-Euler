#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
#left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from PrimesTo import PrimesTo
primes=set(PrimesTo(1000000))

def isTruncatable(x):
    for y in range(1,len(str(x))):
        #print(x)
        if int(str(x)[y:]) not in primes:
            #print(int(str(x)[y:]))
            return(False)
        if int(str(x)[:y:]) not in primes:
            #print(int(str(x)[y::-1]))
            return(False)
    return(True)
n=0
count=0
for x in primes:
    if count==11:
        break
    if isTruncatable(x)==True and len(str(x))>1:
        n=n+x
        count=count+1


print(n)