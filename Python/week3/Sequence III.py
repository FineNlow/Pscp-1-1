"""Sequence III"""
def sequence(x):
    """Sequence III"""
    for i in range(2, x+2):
        for j in range(x):
            print(i + j, end=" ")
        print()
sequence(int(input()))
