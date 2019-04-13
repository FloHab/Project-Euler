#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import time
start_time = time.clock()
for a in range(1000):
    for b in range(1000):
        if a>0 and b>a and a+b+(a**2+b**2)**(0.5)==1000:
            print(a)
            print(b)
            print((a**2+b**2)**(0.5))
            print(a*b*(a**2+b**2)**(0.5))
print(time.clock() - start_time, "seconds")