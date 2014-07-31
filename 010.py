"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


def findPrimes(max_number):
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
	return sum(findPrimes(number))

if __name__=="__main__":
	print (solve(2000000))

