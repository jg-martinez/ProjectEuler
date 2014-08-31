"""
Project Euler Problem #15
==========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def binomial_coefficient(a, b):
    return factorial(a+b)/(factorial((a+b)-a)*factorial(a))

def solve():
    print(binomial_coefficient(20,20))

if __name__=="__main__":
    solve()

