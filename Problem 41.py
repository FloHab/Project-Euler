#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
#2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?
from itertools import permutations
from isPrime import isPrime
x=[1,12,123,1234,12345,123456,1234567,12345678,123456789]
permut=[]

for y in x:
    perm=[''.join(p) for p in permutations(str(y))]
    permut=permut+perm
prime=0
for x in permut:
    if isPrime(int(x))==True and int(x)>int(prime):
        prime=x
        print(x)

print(prime)