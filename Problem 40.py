#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


decimalFraction=''
for x in range(1,200000):
    decimalFraction=decimalFraction+str(x)

print(len(decimalFraction))

print(int(decimalFraction[0])*int(decimalFraction[9])*int(decimalFraction[99])*int(decimalFraction[999])*int(decimalFraction[9999])*int(decimalFraction[99999])*int(decimalFraction[999999]))