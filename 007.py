"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""
import math


def findPrimes():
	max_number = 1000000
	is_composite = [False for x in range(max_number)]
	for i in range (4, max_number, 2):
		is_composite[i] = True
	next_prime = 3
	stop_at = math.sqrt(max_number)
	while (next_prime < stop_at):
		for i in range(next_prime * 2, max_number, next_prime):
			is_composite[i] = True
		next_prime = next_prime + 2
		while ((next_prime <= max_number) and is_composite[next_prime]):
			next_prime = next_prime + 2
	primes = []
	for i in range(2, max_number):
		if (not is_composite[i]):
			primes.append(i)
	return primes

def solve(number):
	list_primes = findPrimes()
	return list_primes[number]

if __name__=="__main__":
	print(solve(10000))

