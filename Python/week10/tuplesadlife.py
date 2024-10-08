"""tuplesaddy"""
def tupp():
    """tupp"""
    tup = tuple(input().split())
    char = input()
    char_index = tup.index(char)
    char_count = tup.count(char)
    for _ in range(char_count):
        for _ in range(char_count):
            print(char_index, end=" ")
        print()
tupp()
