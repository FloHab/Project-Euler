#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#    1634 = 14 + 64 + 34 + 44
#    8208 = 84 + 24 + 04 + 84
#    9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import time
start_time = time.clock()
z=[]

def sum_of_powers(x):
    summe=0
    for y in str(x):
        summe=summe+int(y)**5
    return(summe)

for x in range(2,354294):
    if x ==sum_of_powers(x):
        z.append(x)

print(sum(z))
print(time.clock() - start_time, "seconds")