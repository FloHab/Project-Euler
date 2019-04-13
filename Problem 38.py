#Take the number 192 and multiply it by each of 1, 2, and 3:
#    192 × 1 = 192
#    192 × 2 = 384
#    192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
#of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
#which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
#(1,2, ... , n) where n > 1?
import time
start_time = time.clock()
def isPandigital(number):
    x="".join(sorted(str(number)))
    if x=="123456789":
        return True
    else:
        return False

pandigitals=[]
ns=[]
for x in range(1,10000):
    string=""
    n=1
    while len(string)<9:
        string=string+str(x*n)
        n=n+1
    if isPandigital(int(string))==True:
        pandigitals.append((int(string)))
        ns.append(x)

print(max(pandigitals))
print(time.clock() - start_time, "seconds")