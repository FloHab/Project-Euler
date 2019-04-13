#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
import time
start_time = time.clock()
count_max=0
count=1
numbers=list(range(1000000))
Liste={}
for y in numbers:
    n=y
    if count > count_max:
        count_max = count
        n_max = y-1
    count = 1
    while n>1:
        count = count + 1
        if n in Liste:
            count = count + Liste[n]
            Liste[y] = count
            break
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
#Trage die Kette in die Liste ein
    if y not in Liste:
        Liste[y]=count

print(time.clock() - start_time, "seconds")
print(count_max)
print(n_max)