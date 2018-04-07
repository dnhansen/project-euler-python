from functools import reduce

def gcd(x,y):
    # Euclidean algorithm
    if x == y:
        return x     
    else:
        minimum = min(x,y)
        maximum = max(x,y)
        remainder = maximum % minimum

        if remainder == 0:
            return minimum
        else:
            return gcd(remainder, min(x,y))


def lcm(x,y):
    return int(x*y / gcd(x,y))


nums = range(1,21)
lcm_val = reduce(lcm, nums)
print(lcm_val)
