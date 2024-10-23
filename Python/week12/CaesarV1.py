"""CaesarV1"""
def main():
    """Kuy nang kid decode yang nan"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoder = ""
    shift = int(input())
    for i in input():
        if i.islower():
            position = (alphabet.index(i) + shift) % 26
            decoder += alphabet[position]
        elif i.isupper():
            position = (alphabet.index(i.lower()) + shift) % 26
            decoder += alphabet[position].upper()
        else:
            decoder += i
    print(decoder)
main()
