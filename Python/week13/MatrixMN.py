"""Matrix"""
def main(m, n):
    """Mat"""
    matrix = [[input() for _ in range(n)] for _ in range(m)]
    for num in matrix:
        print(*num)
main(int(input()), int(input()))
