#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
#amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

import time
start_time = time.clock()
list_divisors=[]
Sum_proper_div={}
for x in range(2,10002):
    Sum_proper_div.update({x-1:sum(list_divisors)})
    list_divisors=[]
    for y in range(1,x):
        if x%y==0:
            list_divisors.append(y)
amicable_numbers=[]

for x in Sum_proper_div:
    for y in Sum_proper_div:
        if x==Sum_proper_div[y] and Sum_proper_div[x]==y and x!=y:
            if x not in amicable_numbers and y not in amicable_numbers:
                amicable_numbers.append(x)
                amicable_numbers.append(y)

print(amicable_numbers)
print(sum(amicable_numbers))

print(time.clock() - start_time, "seconds")