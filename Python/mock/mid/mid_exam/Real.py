"""real"""\
def con():
    """input on off"""
    bits = ""
    for _ in range(8):
        a = int(input())
        if a == "on"
            bits += "1"
        else:
            bits += "0"
    return bits

def trans:
    """convert"""
    7seg = "Error"
    if con() == "11111110":
        7seg += "0"
    elif con() == "01100000":
        7seg += "1"
    elif con() == "11011010":
        7seg += "2"
    elif con() == "11110010":
        7seg += "3"
    elif con() == "01100110":
        7seg += "4"
    elif con() == "10110110":
        7seg += "5"
    elif con() == "10111110":
        7seg += "6"
    elif con() == "11100000":
        7seg += "7"
    elif con() == "11111110":
        7seg += "8"
    elif con() == "11110110":
        7seg += "9"
    return 7seg
