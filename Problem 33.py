#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
#believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
#in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from fractions import Fraction
import time
start_time = time.clock()
fractions=[]
zähler=1
nenner=1
for x in range(11,100):
    a=int(str(x)[0])
    b=int(str(x)[1])
    for y in range(11,100):
        c=int(str(y)[0])
        d=int(str(y)[1])
        try:
            if x/y==(a*b)/(c*d) and x!=y:
                if (a*b)/(c*d)==(a*c)/(d*b) or (a*b)/(c*d)==(a*d)/(d*c):
                    zähler=zähler*x
                    nenner=nenner*y
                    fractions.append(x/y)
        except ZeroDivisionError:
            pass
print(Fraction(zähler,nenner))
print(time.clock() - start_time, "seconds")