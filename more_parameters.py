'''
simple_programming_

This code defines a function with unknown
number of parameters and calls it 
'''
def summation(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)