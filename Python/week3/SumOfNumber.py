"""SumOfNumber"""
def sumznum(target):
    """SumOfNumber"""
    sumz = 0
    while True:
        y = int(input())
        if y == -1:
            break
        sumz += y
        if sumz == target:
            break
    print(sumz)
sumznum(int(input()))
