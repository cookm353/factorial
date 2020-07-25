# !/usr/bin/env python3

# factorial_3_ways.py
# first time using assert, so it's a little sloppier than I'd like
# m. cook

from functools import reduce
import numpy as np


N = 4


def build_num_list():
	"""
	Create a list of numbers based on its sign
	"""

	if N > 0:
		return list(range(1, N + 1))
	elif N < 0:
		return list(range(N, 0))
	elif N == 0:
		return N


def numpy_factorial(num_list):
	"""
	Using a NumPy aggregate ufunc
	"""
	num_list = np.array(num_list)

	return np.multiply.reduce(num_list)


def functools_reduce_factorial(num_list):
	"""
	One liner with reduce and a lambda function
	"""
	return reduce((lambda x, y: x * y), num_list)


def loop_factorial(num_list):
	"""
	Brute forcing with a for loop
	"""

	loop_factorial = 1

	for num in num_list:
		loop_factorial *= num

	return loop_factorial


def test_results(np, reduced, for_loop):
	"""
	Verify that all three methods return the same value
	"""
	try:
		assert np == reduced
	except AssertionError:
		print("Error: NumPy and functools.reduce return different values")

	try:
		assert reduced == for_loop
	except AssertionError:
		print("Error: functools.reduce() and the for loop return", end=' ')
		print("different values")
		return None
	else:
		return np


def main():
	# Storing number list to be passed as argument
	num_list = build_num_list()

	# Check whether or not N is 0
	if not N:
		print(1)
	else:
		# Store results of each function
		np_factorial = numpy_factorial(num_list)
		reduce_factorial = functools_reduce_factorial(num_list)
		brute_force = loop_factorial(num_list)

		# Test if they're all correct
		factorial = test_results(np_factorial, reduce_factorial, brute_force)

		if factorial:
			print(factorial)


if __name__ == "__main__":
	main()