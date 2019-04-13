#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)
z=0
for x in range(1000000):
    if str(x)==str(x)[::-1]:
        if str(bin(x))[2::]==str(bin(x))[:1:-1]:
            z=z+x

    else:
        pass





#print(str(bin(585))[2::])
#x=str(bin(585))[:1:-1]
#print(x)
print(z)