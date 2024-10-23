"""Is_prime"""
def is_prime(n):
    """Kuy"""
    if n <= 1:
        return "False"
    for i in range(2, int(n**0.5) + 1,3):
        if not n % i:
            return "False"
    return "True"
print(is_prime(int(input())))
