"""Lab"""
def main(x):
    """Lab"""
    last_num = [7, 9, 3, 1]
    return last_num[x % 4 - 1]
x2 = int(input())
print(main(x2))
