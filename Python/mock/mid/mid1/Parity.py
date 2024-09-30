"""Parity"""
def parity(bits, text):
    """Parity"""
    count = 0
    bits_add = ""
    for i in bits:
        if i == "1":
            count += 1
    if text == "Even":
        if not count%2:
            bits_add = "0"
        else:
            bits_add = "1"
    elif text == "Odd":
        if not count%2:
            bits_add = "1"
        else:
            bits_add = "0"
    result = bits + bits_add
    print(result)
parity(input(), input())
