"""coke"""
from math import ceil
def coke(a, b, c, d):
    """coke kaeng puy"""
    if not b:
        price = d*a
    elif not d:
        price = 0
    else:
        price = ((a * d) - (ceil((d - b)/ b)*(a - c)))
    print(price)
coke(int(input()), int(input()), int(input()), int(input()))
