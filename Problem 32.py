#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
#the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
#through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import time
start_time = time.clock()
digits=[1,2,3,4,5,6,7,8,9]
digits_two=[1,2,3,4,5,6,7,8,9]
list_multiplicant=[]
list_multiplier=[]
list_products=[]
'Multiplicand 2 digits; multiplier 3 digits, product 4 digits'
for x in digits:
    for y in digits:
        for a in digits:
            for b in digits:
                for c in digits:
                    if x!=y and x!=a and x!=b and x!=c and y!=a and y!=b and y!=c and a!=b and a!=c and b!=c:
                        multiplicant=str(x)+str(y)
                        multiplier=str(a)+str(b)+str(c)
                        list_multiplicant.append(multiplicant)
                        list_multiplier.append(multiplier)

for x in digits:
    for y in digits:
        for a in digits:
            for b in digits:
                for c in digits:
                    if x!=y and x!=a and x!=b and x!=c and y!=a and y!=b and y!=c and a!=b and a!=c and b!=c:
                        multiplicant=str(x)
                        multiplier=str(y)+str(a)+str(b)+str(c)
                        list_multiplicant.append(multiplicant)
                        list_multiplier.append(multiplier)



for x in range(len(list_multiplicant)):
    product=(int(list_multiplicant[x]))*(int(list_multiplier[x]))
    list_products.append(str(product))


pandigital=[]

for x in range(len(list_multiplicant)):
    every_thing=list_multiplier[x]+list_multiplicant[x]+list_products[x]
    count=0
    for y in digits:
        if len(every_thing)>9:
            break
        if (every_thing.count(str(y)))!=1:
            break
        else:
            count=count+1
        if count==9:
            if int(list_products[x]) not in pandigital:
                pandigital.append(int(list_products[x]))
print(sum(pandigital))

print(time.clock() - start_time, "seconds")