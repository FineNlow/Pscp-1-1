"""bill"""
def bill(price):
    """bill"""
    charge = 0.1 * price
    if charge < 50:
        charge = 50
    if charge > 1000:
        charge = 1000
    total = ((price+charge)*0.07)+charge+price
    print(f"{total:.2f}")
bill(int(input()))
