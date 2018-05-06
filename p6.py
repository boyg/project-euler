'''
Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
'''
n = 100

'''Using Faulhaber's formula for the p = 1 and p = 2 cases'''
sum_of_squares = n * (n+1) * (2*n+1) / 6
square_of_sum = (n * (n+1) / 2) ** 2

print(square_of_sum - sum_of_squares)
