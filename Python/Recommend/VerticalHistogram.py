"""VerticalHistogram"""
def vh(text):
    """EEIEIIE"""
    alpha = []
    nn = []
    # input
    for char in text:
        if char.isalpha():
            alpha.append(char)
        if char not in nn:
            nn.append(char)
    # count
    for same in alpha:
        for check in nn:
            if check == same:
    
vh(input().strip().replace(" ",""))
