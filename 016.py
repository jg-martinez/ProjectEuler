"""
Project Euler Problem #16
==========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import math


def sum_digits(num):
    result_pow = int(math.pow(2, num))
    res = 0
    for i in str(result_pow):
       res += int(i)
    return res

def solve():
    print(sum_digits(1000))

if __name__=="__main__":
    solve()
