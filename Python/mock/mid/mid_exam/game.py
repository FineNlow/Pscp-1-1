"""game"""
def game(a,b):
    """game"""
    print(b%3 if a%3 == b%3 else "Error")
game(int(input()),int(input()))
