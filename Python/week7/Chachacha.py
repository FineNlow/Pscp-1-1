"""Cha cha cha"""
from math import ceil
def cha(dn):
    """Cha cha cha"""
    h = 0
    for _ in range(1, dn+1):
        h += ceil(float(input())) * 8720
    print(f"{h:.0f}")
cha(int(input()))
