"""Post"""
def post(n,m):
    """Post"""
    total = 0
    delivery = 0
    for _ in range(n):
        env = float(input())
        if 0 < env <= 10:
            total += 16
        elif 10 < env <= 20:
            total += 18
        elif 20 < env <= 100:
            total += 23
        elif 100 < env <= 250:
            total += 28
        elif 250 < env <= 500:
            total += 33
        elif 500 < env <= 1000:
            total += 48
        elif 1000 < env <= 2000:
            total += 68
        delivery += 13
    for _ in range(m):
        pkg = float(input())
        if 0 < pkg <= 500:
            total += 45
        elif 500 < pkg <= 1000:
            total += 55
        elif 1000 < pkg <= 2000:
            total += 70
        delivery += 15
    print(int(total + delivery))
post(int(input()), int(input()))
