"""Homerun"""
def home(n, dis):
    """Homerun"""
    run = 0
    for _ in range(n):
        if float(input()) < dis:
            run += 1
    print(run)
home(int(input()), float(input()))
