"""loopkwaikwai"""
def sequencev(n):
    """loopkwaikwai"""
    for i in range(n, 0, -1):
        print(i, end=" ")
        if not (n - i + 1) % 7:
            print()
sequencev(int(input()))
