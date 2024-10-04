"""Tax"""
def tax(year, engine):
    """Tax"""
    total = 0
    if 1 <= engine <= 600:
        total += engine * 0.5
    elif 600 < engine <= 1800:
        total += 600 * 0.5
        total += (engine - 600) * 1.5
    elif engine > 1800:
        total += 600 * 0.5
        total += (1800 - 600) * 1.5
        total += (engine - 1800) * 4
    if year == 6:
        total -= total * 0.1
    elif year == 7:
        total -= total * 0.2
    elif year == 8:
        total -= total * 0.3
    elif year == 9:
        total -= total * 0.4
    elif year >= 10:
        total -= total * 0.5
    print(f"{total:.2f}")
tax(int(input()),int(input()))
