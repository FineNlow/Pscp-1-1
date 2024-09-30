"""HowLong"""
def howlong(x):
    """HowLong"""
    cnt = 0
    for _ in str(x):
        cnt += 1
    print(cnt)
howlong(abs(int(input())))
