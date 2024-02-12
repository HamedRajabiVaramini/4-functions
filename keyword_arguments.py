'''
simple_programming_

This code defines a function with a
parameter and calls it arbitrary keyword
arguments 
'''
def printName(**names):
    for key in names:
        print(names[key])

printName(firstName = "Bill", lastName = "Gates")