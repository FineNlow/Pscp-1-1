"""GCD"""
def gcd(a, b):
    """ggg"""
    while b:
        a, b = b, a % b
    return a
num1, num2 = int(input()), int(input())
print(f"YES\n{gcd(num1,num2)}" if gcd(num1, num2) == 1 else f"NO\n{gcd(num1,num2)}")
