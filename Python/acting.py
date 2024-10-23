"""Matrix"""
def main():
    """Mat"""
    m, n = int(input()), int(input())
    matrix = []
    for _ in range(m):
        row = [int(input()) for _ in range(n)]
        matrix.append(row)
    for num in matrix:
        print(*num)
main()
