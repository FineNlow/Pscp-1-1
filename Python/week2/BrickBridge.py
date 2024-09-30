"""BrickBridge"""
def brick(a, b, goal):
    """BrickBridge"""
    max_b = goal // 5
    if b > max_b:
        b = max_b
    plus = (b*5) + a
    if plus >= goal:
        total = goal - (b*5)
        print(total)
    elif plus < goal:
        print(-1)
brick(int(input()), int(input()), int(input()))
