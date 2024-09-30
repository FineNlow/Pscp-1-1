"""Bad Keyboard"""
def bk(text):
    """keyboardkwaikwai"""
    nt = ""
    for ch in text:
        if ch == "i":
            nt += "o"
        elif ch == "o":
            nt += "i"
        elif ch == "I":
            nt += "O"
        elif ch == "O":
            nt += "I"
        else:
            nt += ch
    print(nt)
bk(input())
