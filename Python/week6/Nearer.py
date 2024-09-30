"""Nearer"""
def nearer(ax, bx, cx):
    """Nearer"""
    x_ax = abs(cx - ax)
    x_bx = abs(cx - bx)
    if x_ax < x_bx:
        print(f"Alice {x_ax}")
    elif x_bx < x_ax:
        print(f"Bob {x_bx}")
    else:
        print(f"Sundaes {x_ax}")
nearer(int(input()), int(input()), int(input()))
