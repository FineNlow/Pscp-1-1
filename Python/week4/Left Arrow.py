"""Left Arrow"""
def leftarrow(k, n):
    """Left Arrow"""
    z = n // 2
    space = z
    for _ in range(n):
        print((space*" ")+(k * "*") )
        space = abs(z -1)
        z -= 1
leftarrow(int(input()), int(input()))
