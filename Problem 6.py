#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers=list(range(1,101))
print(numbers)
squares=[]
for x in numbers:
    squares.append(x*x)

sum_of_squares=sum(squares)
square_of_sum=(sum(numbers))*(sum(numbers))
print(sum_of_squares)
print(square_of_sum)
print(squares)
print(square_of_sum-sum_of_squares)
