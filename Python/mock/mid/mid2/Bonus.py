"""Bonus"""
def bonus(s, y, m):
    """Bonus"""
    if 10 <= m <= 12:
        y += 1
    if y >= 20:
        y = 20
    total_bonus = s * y
    if total_bonus >= 1000000:
        total_bonus = 1000000
    elif total_bonus <= 5000:
        total_bonus = 5000
    print(total_bonus)
bonus(abs(int(input())), abs(int(input())), abs(int((input()))))
