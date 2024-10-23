"""CaesarV2"""
def main():
    """Kuy nang kid decode yang nan"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoder = ""
    eng = ["what", "when", "why", "which", "this", "there", "where", "the",\
           "is", "am", "are", "you", "we", "they", "he", "she", "it"]
    for i in input():
        shift = 0
        if decoder.lower() not in eng:
            if i.islower():
                position = (alphabet.index(i) + shift) % 26
                decoder += alphabet[position]
            elif i.isupper():
                position = (alphabet.index(i.lower()) + shift) % 26
                decoder += alphabet[position].upper()
            else:
                decoder += i
            shift += 1
    print(decoder)
main()
