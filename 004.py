"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindrome(number):
	return str(number) == str(number)[::-1]
	
def solve():
	result = 0
	for i in range(999,100,-1):
		for j in range(999, 100, -1):
			if (isPalindrome(i*j) and (i*j) > result):
				result = i * j
	return result

if __name__=="__main__":
	print (solve())