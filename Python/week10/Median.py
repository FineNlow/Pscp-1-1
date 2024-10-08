"""Median"""
def med():
    """Median"""
    lst = []
    for _ in range(int(input())):
        lst.append(float(input()))
    lst.sort()
    if len(lst) % 2:
        print(f"{(lst[len(lst)//2]):.3f}")
    else:
        print(f"{((lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2):.3f}")
med()
