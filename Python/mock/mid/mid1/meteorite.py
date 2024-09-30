"""Meteorite"""
def count_beam(a, b, c):
    """Meteorite"""
    beam = 0
    while a >= c:
        a = a / b
        beam += 1
    print(beam)
count_beam(float(input()),int(input()),float(input()))
