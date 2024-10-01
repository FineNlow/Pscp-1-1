"""Password"""
from math import log2
def calculate_entropy(password):
    """Password"""
    R = 0
    L = len(password)
    if any('a' <= char <= 'z' for char in password):
        R += 26
    if any('A' <= char <= 'Z' for char in password):
        R += 26
    if any(char.isdigit() for char in password):
        R += 10
    special_characters = "~`!@#$%^&*()-_=+{}[]|\\:;\"'<>,.?/"
    if any(char in special_characters for char in password):
        R += 32
    return log2(R**L)

def pass_level(entropy):
    """Check password level"""
    if entropy < 28:
        return "Very Weak"
    if 28 <= entropy < 36:
        return "Weak"
    if 36 <= entropy < 60:
        return "Reasonable"
    if 60 <= entropy < 128:
        return "Strong"
    return "Very Strong"

def main():
    """input and print"""
    user_password = input()
    calculated_entropy = calculate_entropy(user_password)
    print(int(calculated_entropy))
    print(pass_level(calculated_entropy))
main()
