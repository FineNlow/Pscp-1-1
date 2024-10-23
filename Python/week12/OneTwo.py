"""OneTwo"""
def ot(n):
    """OneTwo"""
    if n == 1:
        return "1"
    if n == 2:
        return "2"
    return ot(n-1) + ot(n-2)
print(ot(int(input())))
