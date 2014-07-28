"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math


def findFactors(number):
	factors = []
	while (number % 2 == 0):
		factors.append(2)
		number = number/2
	i = 3
	max_factor = math.sqrt(number)
	while (i <= max_factor):
		while (number % i == 0):
			factors.append(i)
			number = number/i
			max_factor = math.sqrt(number)
		i = i + 2
	if (number > 1):
		factors.append(number)
	return factors

def maxFactor(list_factors):
	return int(max(list_factors))
	
if __name__=="__main__":
	print(maxFactor(findFactors(600851475143)))
	
