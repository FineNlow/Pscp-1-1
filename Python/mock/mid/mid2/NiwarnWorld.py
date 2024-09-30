"""Niwarn World"""
from math import sin, log, radians
def niwarn(n, s, k):
    """Niwarn World"""
    def x(n):
        """x"""
        form1 = 2 + (log(n**2, 2) / ((2 * n) * log(n, 2)))
        return form1
    
    def y(n, s):
        """y"""
        form2 = (sin(radians(30)) + ((2 * s) ** 0.5)) / (x(n) + 3)
        return form2
    
    def z(k):
        """z"""
        form3 = (y(k, k) ** 2) + (8456 * (x(k) ** 4)) / (24 * k)
        return form3
    
    print(f"X: {x(n):.1f}, Y: {y(n, s):.1f}, Z: {z(k):.1f}")

niwarn(float(input()), float(input()), float(input()))
