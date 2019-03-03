with open("pe_013.txt", "r") as f:
	data = f.readlines()

print(str(sum([int(n) for n in data]))[0:10])