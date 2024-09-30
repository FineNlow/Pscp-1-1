"""Squidgame"""
def game():
    """Squidgame"""
    total_a = 0
    total_b = 0
    for _ in range(10):
        a = int(input())
        total_a += a
    for _ in range(10):
        b = int(input())
        total_b += b
    if total_a < total_b:
        print("A")
    elif total_a > total_b:
        print("B")
    elif total_a == total_b:
        print("AB")
game()
