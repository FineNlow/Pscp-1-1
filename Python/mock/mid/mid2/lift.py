"""lift"""
def lift(n, lw):
    """Depressed lift"""
    total_hw = 0
    a = 0
    k = 0
    for _ in range(n):
        age = int(input())
        hw = abs(float(input()))
        total_hw += hw
        a += 1 if age >= 12 else 0
        k += 1 if age < 12 else 0
    print("Not Safe" if total_hw > lw or k and not a else "Safe")
lift(int(input()), abs(float(input())))
