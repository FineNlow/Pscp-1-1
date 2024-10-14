"""PST"""
def ps():
    """Point Sorting function"""
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            x, y = map(int, input().split())
            points.append((x, y))
        points.sort(key=lambda p: (p[0] + p[1], -p[1]))
        for point in points:
            print(point[0], point[1])
ps()
