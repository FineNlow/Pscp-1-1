"""Heron of Alexandria"""
from math import sqrt
def formula():
    """Heron of Alexandria"""
    a,b,c = float(input()),float(input()),float(input())
    s = (a+b+c) / 2
    area = sqrt(((s*s)-(s*a))*(s-b)*(s-c))
    print(f"{area:.3f}")
formula()
