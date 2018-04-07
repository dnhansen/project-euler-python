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

n = 2000000-1

prime_sum = sum(primes(n))
print(prime_sum)
