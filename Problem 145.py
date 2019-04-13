#Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
#For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are
#reversible. Leading zeroes are not allowed in either n or reverse(n).
#There are 120 reversible numbers below one-thousand.
#How many reversible numbers are there below one-billion (10**9)?
import time


#Zweistelling:
#10a+b
20
#Dreistellig:
#100(a+c)+10(2b)+(a+c)
20*10
#Vierstellig:
#1000(a+d)+100(c+b)+10(c+b)+(a+d)

#Fünfstellig:
'Nicht möglich'

#Sechstellig:
#100000(a+f)+10000(b+e)+1000(c+d)+100(c+d)+10(b+e)+(a+f)

#Achtstellig:
#10000000(a+h)+1000000(b+g)+100000(c+f)+10000(d+e)+1000(d+e)+100(c+f)+10(b+g)+(a+h)


print(zwei)
print(drei)
print(vier)
print(time.clock() - start_time, "seconds")