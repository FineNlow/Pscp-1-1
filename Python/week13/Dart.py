"""Dart"""
def dart():
    """Dart"""
    score = 0
    for _ in range(int(input())):
        x, y = input().split()
        d = (int(x)**2 + int(y)**2)**0.5
        if d <= 2:
            score += 5
        elif 2 < d <= 4:
            score += 4
        elif 4 < d <= 6:
            score += 3
        elif 6 < d <= 8:
            score += 2
        elif 8 < d <= 10:
            score += 1
    print(score)
dart()
