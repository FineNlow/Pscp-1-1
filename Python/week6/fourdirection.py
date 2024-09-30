"""4d"""
def main(mark):
    """code kod D in below"""
    line1, line2, line3, line4, line5 = "", "", "", "", ""
    for arrow in mark:
        if arrow == "U":
            line1 += "  *   "
            line2 += " ***  "
            line3 += "* * * "
            line4 += "  *   "
            line5 += "  *   "
        elif arrow == "D":
            line1 += "  *   "
            line2 += "  *   "
            line3 += "* * * "
            line4 += " ***  "
            line5 += "  *   "
        elif arrow == "L":
            line1 += "  *   "
            line2 += " *    "
            line3 += "***** "
            line4 += " *    "
            line5 += "  *   "
        elif arrow == "R":
            line1 += "  *   "
            line2 += "   *  "
            line3 += "***** "
            line4 += "   *  "
            line5 += "  *   "
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
main(input())
