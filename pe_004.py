def is_palindrome(n):
    n_original = [d for d in str(n)]
    inverse = n_original[::-1]
    if n_original == inverse:
        return True
    else:
        return False

max = 0

for i in range(999,99,-1):
    for j in range(999,i-1,-1):
        prod = i*j
        if prod > max and is_palindrome(prod):
            max = prod
            break

print(max)
