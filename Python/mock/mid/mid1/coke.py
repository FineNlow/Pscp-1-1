"""coke"""
def coke():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    cost = 0

    if b == 0 or b > d:
        cost = a * d
    else:
        regular_price_bottles = d // b
        remaining_bottles = d % b
        
        cost = (regular_price_bottles * b * a) + (regular_price_bottles * c) + (remaining_bottles * a)

        total_bottles_with_discount = (regular_price_bottles + 1) * b

        if total_bottles_with_discount <= d:
            cost = min(cost, total_bottles_with_discount * c + (d - total_bottles_with_discount) * a)

    print(cost)
coke()
