def is_prime(number):
    """Check if a number is prime"""
    if number in (2, 3):
        return True
    if number == 1 or number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def all_primes_finder(number):
    """Find all prime numbers from 2 to sqrt(number)"""
    all_primes = []
    for prime in range(2, int(number ** 0.5) + 1):
        if is_prime(prime):
            all_primes.append(prime)
    return all_primes

def factoring(amount):
    """Perform prime factorization for multiple numbers"""
    for _ in range(amount):
        prime_dict = {}
        number = int(input())
        if is_prime(number):
            print(number)
            continue
        all_primes = all_primes_finder(number)
        divisor = number
        while divisor > 1:
            if divisor in all_primes:
                prime_dict[int(divisor)] = prime_dict.get(divisor, 0) + 1
                break
            for prime in all_primes:
                if divisor % prime == 0:
                    prime_dict[prime] = prime_dict.get(prime, 0) + 1
                    divisor /= prime
                    break
        my_list = [str(key) if value == 1 else str(key) + "**" + str(value) for key, value in prime_dict.items()]
        print(" x ".join(my_list))

factoring(int(input()))
