"""CoinChangev1"""
def cc(changes):
    """CoinChangev1"""
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while coin <= changes:
            changes -= coin
            count += 1
    print(count)
cc(int(input()))
