#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
n=4
primes=[2,3]
factors=[]
while len(primes)<10001:
    print(len(primes))
    for x in range(1,int(n/2+1)):
        if n%x==0:
            factors.append(x)
    if sum(factors)==1:
        primes.append(n)
        n=n+2
        factors=[]
    else:
        n=n+1
        factors=[]
print(primes[-1])

