"""LineSorting"""
def sorting():
    """LineSorting"""
    lst = [input() for _ in range(int(input()))]
    print(i for i in sorted(lst,key=len))
sorting()
