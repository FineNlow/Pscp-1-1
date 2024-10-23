"""kabata"""
def trans():
    """kuy"""
    for _ in range(int(input())):
        text = input().replace("baka", " ").replace("bakka", "").replace("ka", "")\
        .replace("ba", "").replace("ta", "")
        print("yes" if not text else "no")
trans()
