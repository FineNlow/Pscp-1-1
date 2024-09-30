"""Pringles"""
def pringles(up_part, crisp, down_part, finger):
    """visualize those pringles in the can"""
    crispCnt = 0
    newCrisp = ""
    for pieces in crisp:
        if finger > 0:
            if pieces == ")":
                crispCnt += 1
            newCrisp += " "
        else:
            newCrisp += pieces
        finger -= 1
    print(crispCnt)
    if newCrisp.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(up_part, newCrisp, down_part, sep="\n")
pringles(input(), input(), input(), int(input()))
