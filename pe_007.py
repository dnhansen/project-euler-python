import math

def primes(n):
    # Gets the first n primes
    if n == 1:
        return [2]
    else:
        prime_list = [2]
        
        k = 3

        while len(prime_list) < n:
            prime = True
            root = math.floor(math.sqrt(k))
            
            for p in prime_list:
                if p > root:
                    break
                elif k % p == 0:
                    prime = False
                    break

            if prime:
                prime_list.append(k)

            k += 1

        return prime_list

prime_list = primes(10001)
print(prime_list[-1])
