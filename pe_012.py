from collections import Counter
from functools import reduce
import operator # In Python 3.8, simply import prod from math

def prod(L):
	return reduce(operator.mul, L, 1)


def counter_add(*L):
	output = Counter()
	for c in L:
		output += c
	return output
	

def factorize(n):
	factors = Counter()

	d = 2

	while n >= d:
		if n % d == 0:
			if d in factors:
				factors[d] += 1
			else:
				factors[d] = 1
			n //= d
		else:
			d += 1

	return(factors)


def divisors(*L):
	factor_counters = [factorize(n) for n in L]
	total_factors = counter_add(*factor_counters)
	return prod([exp+1 for exp in total_factors.values()])


n = 2
while True:
	if n % 2 == 0:
		num_d = divisors(n//2, n+1)
	else:
		num_d = divisors(n, (n+1)//2)

	print(n, num_d)
	if num_d >= 500:
		break

	n += 1