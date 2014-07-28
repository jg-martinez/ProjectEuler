"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
def gcd(a,b):
	while (b != 0):
		remainder = a % b
		a = b
		b = remainder
	return a
	
def solve():
	list_numbers = [x for x in range(3,21)]
	result = 2
	for x in list_numbers:
		result = result * x / gcd(result, x)
	return int(result)

if __name__=="__main__":
	print(solve())

