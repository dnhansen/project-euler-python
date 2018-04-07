from functools import reduce

filename = 'pe_python_008.txt'

file = open(filename)
number = file.read().replace('\n', '')

length = len(number)
n = 13

maximum = 0

for i in range(length-n):
    digits = number[i:i+n]
    product = reduce(lambda x,y: int(x)*int(y), digits)

    if product > maximum:
        maximum = product

print(maximum)
