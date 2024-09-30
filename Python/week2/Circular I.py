"""Circular I"""
import math
def main():
    """Circular I"""
    ix = float(input())
    iy = float(input())
    r = float(input())
    mx = float(input())
    my = float(input())
    rf = float(input())
    d = math.sqrt((mx - ix) ** 2 + (my - iy) ** 2)
    if d <= r:
        print("Yes")
    else:
        print("No")
main()
