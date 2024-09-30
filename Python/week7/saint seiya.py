"""saint seiya"""
def punch():
    """saint seiya"""
    timer = int(input())
    goal_punch = int(input())
    punches_count = 0
    for i in range(2, timer + 1, 2):
        if punches_count < goal_punch:
            if not i % 6:
                punches_count += 1
            elif not i % 2:
                punches_count += 165
        else:
            punches_count += (timer + 1 - i) * 12
            break
    print(punches_count)
punch()
