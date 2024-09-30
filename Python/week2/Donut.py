"""Donut"""
def donut():
    """Donut"""
    a,b,c,d = abs(int(input())), abs(int(input())), abs(int(input())), abs(int(input()))
    box = d // (b+c)
    price = box*b*a
    buy = (b+c)*box
    remain = d-buy
    if remain >= b:
        buy += b+c
        price += b*a
    else:
        buy += remain
        price += remain*a
    print(f"{price} {buy}")
donut()
