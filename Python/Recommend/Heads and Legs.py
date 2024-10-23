"""Two steps ahead"""
def grong(a, b):
    """EIEI"""
    rab = (b - 2 * a) // 2
    bird = a - rab
    print("Impossible" if (b - 2 * a)%2 or rab < 0 or bird < 0 else f"{rab} {bird}")
grong(int(input()), int(input()))
