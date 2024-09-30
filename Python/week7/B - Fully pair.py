"""Pair"""
def pair(char):
    """Pair"""
    get_abandoned = ""
    check = ""
    for text in char:
        if check.count(text) <= 0:
            check += text
    for text in check:
        if char.count(text)%2:
            get_abandoned += text
    print(get_abandoned if get_abandoned else "fully paired")
pair(input())
