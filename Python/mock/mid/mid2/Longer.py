"""longer"""
from math import pi
def long(r,a,b):
    """longer"""
    diff = abs((2*pi*r)-(2*(a+b)))
    if 2*pi*r > 2*(a+b):
        print("Circle is longer")
    elif 2*pi*r < 2*(a+b):
        print("Rectangle is longer")
    elif 2*pi*r == 2*(a+b):
        print("Equal")
    print(f"{diff:.5f}")
long(float(input()), float(input()), float(input()))
