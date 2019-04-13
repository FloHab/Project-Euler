#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
number_below_10000=list(range(0,1000))
to_sum=[]
for x in number_below_10000:
    if x%3==0:
       to_sum.append(x)
    elif x%5==0:
        to_sum.append(x)
print(sum(to_sum))
