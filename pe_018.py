with open("pe_018.txt", "r") as f:
	file = f.readlines()

triangle = [[int(i) for i in line.split()] for line in file]

def get_longest(row, column):
	current = triangle[row][column]
	return max(current + triangle[row+1][column], current + triangle[row+1][column+1])

for i in range(len(triangle)-2, -1, -1):
	for j in range(len(triangle[i])):
		triangle[i][j] = get_longest(i,j)

print(triangle[0][0])