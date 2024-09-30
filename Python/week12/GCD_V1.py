"""GCD"""
def gcd(a, b):
    """ggg"""
    while b:
        a, b = b, a % b
    return a
num1, num2 = int(input()), int(input())
print(gcd(num1, num2))
