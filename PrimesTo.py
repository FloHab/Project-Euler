#Sieve of Eratosthenes:
#The algorithm works as follows.
    #Create a list l of consecutive integers {2,3,…,N}.
    #Select p as the first prime number in the list, p=2.
    #Remove all multiples of p from the l.
    #set p equal to the next integer in l which has not been removed.
    #Repeat steps 3 and 4 until p**2 > N, all the remaining numbers in the list are primes
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
        if l[x]==True:
            primes.append(x)
    return(primes)

def rotate(strg, n):
    return strg[n:] + strg[:n]