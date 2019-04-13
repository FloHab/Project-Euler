#The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**100

sum=0
for x in range(1,1001):
    print(x)
    sum=sum+(x**x)

print(sum)
print(str(sum)[-10:])