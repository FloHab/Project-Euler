#It is possible to write five as a sum in exactly six different ways:
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
#How many different ways can one hundred be written as a sum of at least two positive integers?

#The basic idea is to devide the problem into smaller subproblems:

#In how many ways can you write x using only the number 2? You can write it in as many was as you can write x using only
#the number 1 plus the number of ways yo can write x-2 using number 1 and 2

#In how many way can you write x using only the numbers 1 to n? You can write it in as many ways as you can write x-n using
#the numbers 1 to n plus the number of ways you can write x using the numbers 1 to n-1

#See also problem 32 as this one can be solved using the same strategie

import time
start_time = time.clock()
dynamic_list=[1]+[0]*100
for x in range(1,100):
    n=0
    for element in dynamic_list:
        if n-x>=0:
            dynamic_list[n]=dynamic_list[n]+dynamic_list[n-x]
        n=n+1

print(dynamic_list[-1])
print(time.clock() - start_time, "seconds")