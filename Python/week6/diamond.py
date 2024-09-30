"""diamond"""
def print_diamond(n):
    """no more art"""
    for i in range(n // 2):
        for _ in range(n // 2 - i):
            print(" ", end="")
        print("*", end="")
        if i > 0:
            for _ in range(2 * i - 1):
                print(" ", end="")
            print("*", end="")
        print()
    print("*" * n)
    for i in range(n // 2 - 1, -1, -1):
        for _ in range(n // 2 - i):
            print(" ", end="")
        print("*", end="")
        if i > 0:
            for _ in range(2 * i - 1):
                print(" ", end="")
            print("*", end="")
        print()
print_diamond(int(input()))
