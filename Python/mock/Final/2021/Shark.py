"""Shark"""
def shark(name):
    """ขี้เกียจจจ"""
    shallow = ["BULL SHARK"]
    twilight = ["CHAIN CATSHARK", "GREAT WHITE SHARK", "GUMMY SHARK", "BLUE SHARK", "MAKO SHARK"]
    midnight = ["FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", "GREENLAND SHARK",\
                "COOKIECUTTER SHARK"]
    abyssal = ["MEGAMOUTH SHARK"]
    if "SHARK" in name:
        if name in shallow:
            print("THE SHALLOW ZONE")
        elif name in twilight:
            print("THE TWILIGHT ZONE")
        elif name in midnight:
            print("THE MIDNIGHT ZONE")
        elif name in abyssal:
            print("THE ABYSSAL ZONE")
        else:
            print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
shark(input())
