nums = range(1,101)
s = sum(nums)**2
p = sum(map(lambda x: x**2, nums))

print(abs(s-p))
