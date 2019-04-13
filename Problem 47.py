#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from getPrimefactors import getPrimefactors
n=0
x=3
cons_ints=set()
while n!=4:
    if len(getPrimefactors(x))==4:
        cons_ints.add(x)
        n=n+1
        x=x+1

    else:
        n=0
        x=x+1
        cons_ints=set()

print(cons_ints)

