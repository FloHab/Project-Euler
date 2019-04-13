#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

digits=3

n_one=999
n_two=999
palindrome=[]
for x in range(100,n_one):
    for y in range(100,n_two):
        palindrom=x*y
        if palindrom==int(str(palindrom)[::-1]):
            palindrome.append(palindrom)
            break
print(max(palindrome))