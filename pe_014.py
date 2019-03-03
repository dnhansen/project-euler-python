import operator

tested = {}

def collatz(n):
	if n == 1:
		return 1
	elif n in tested:
		return tested[n]

	if n % 2 == 0:
		next_n = n // 2
	else:
		next_n = 3*n + 1

	total_length = collatz(next_n) + 1
	tested[n] = total_length
	return total_length


for n in range(1,1000000):
	collatz(n)

print(max(tested.items(), key=operator.itemgetter(1)))