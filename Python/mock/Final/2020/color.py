"""color"""
def color():
    """color"""
    color1, color2 = input(), input()
    mae_sii = ("Red", "Yellow", "Blue")
    if color1 not in mae_sii or color2 not in mae_sii:
        print("Error")
    else:
        if (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
            print("Orange")
        elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
            print("Violet")
        elif (color1 == "Yellow" and color2 == "Blue") or (color1 == "Blue" and color2 == "Yellow"):
            print("Green")
        elif color1 == color2:
            print(color1)
        else:
            print("Error")
color()
