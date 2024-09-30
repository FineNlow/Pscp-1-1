"""sequence1"""
def seq(n):
    """seq"""
    for _ in range(n):
        for j in range(1, n+1):
            print(j, end=" ")
        print()
seq(int(input()))
