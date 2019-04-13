#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
#is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the
#4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?
def PrimesTo(N):
    l={}
    primes=[]
    for x in range(2,N+1):
        l[x]=True
    p=2
    n=2
    while p**2<N:
        while p*n<=N:
            if l[p]==True:
                l[p*n]=False
                n=n+1
            if l[p]==False:
                p=p+1
        p=p+1
        n=2
    for x in l:
        if l[x]==True and len(str(x))==4:
            primes.append(x)
    return(primes)

primes=PrimesTo(9999)
permutations={}

for y in primes:
    for z in primes:
        if z!=y:
            x=z+(z-y)
            if x in primes and (''.join(reversed(sorted(str(x)))))==(''.join(reversed(sorted(str(y))))) and (''.join(reversed(sorted(str(x)))))==(''.join(reversed(sorted(str(z))))):
                print(y)
                print(z)
                print(x)
                print(str(y)+str(z)+str(x))
                primes.remove(y)
                primes.remove(z)
                primes.remove(x)