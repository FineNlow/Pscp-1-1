"""Circular II"""
from math import sqrt
def circularii():
    """Circular II"""
    ix = float(input())
    iy = float(input())
    r = float(input())
    mx = float(input())
    my = float(input())
    rf = float(input())
    d = sqrt((mx - ix) ** 2 + (my - iy) ** 2)
    if d < r + rf:
        print("Yes")
    else:
        print("No")
circularii()
