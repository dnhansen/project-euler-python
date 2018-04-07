import math

def primes(n):
    # Gets primes smaller than or equal to n
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        prime_list = [2]
        
        to_test = range(3,n+1)

        for k in to_test:
            prime = True
            root = math.floor(math.sqrt(k))
            
            for p in prime_list:
                if k % p == 0:
                    prime = False
                    break
                elif p > root:
                    break

            if prime:
                prime_list.append(k)

        return prime_list
    
    

n = 600851475143

root = math.floor(math.sqrt(n))
prime_list = primes(root)
largest_prime_divisor = n

for p in reversed(prime_list):
    if n % p == 0:
        largest_prime_divisor = p
        break

print(largest_prime_divisor)
