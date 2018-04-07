from functools import reduce

def prod(lst):
    return reduce((lambda x,y: x*y), lst)

filename = 'pe_python_011.txt'
file = open(filename)

grid = []

for line in file:
    line_list = line.split(' ')
    line_int = list(map(int, line_list))
    grid.append(line_int)

file.close()

rows = len(grid)
cols = len(grid[0])

n = 4
product = 0

for i in range(1, rows-n):
    for j in range(1, cols-n):
        # Horizontal
        hor = prod([grid[i][j+d] for d in range(n)])
        if hor > product:
            product = hor

        # Vertical
        ver = prod([grid[i+d][j] for d in range(n)])
        if ver > product:
            product = ver

        # Diagonal 1
        dia1 = prod([grid[i+d][j+d] for d in range(n)])
        if dia1 > product:
            product = dia1

        # Diagonal 2
        dia1 = prod([grid[i+d][j+n-d] for d in range(n)])
        if dia1 > product:
            product = dia1
        
print(product)
