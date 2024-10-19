"""Helloooo"""
def main(word):
    """Kyai"""
    vowels = 'aeiouAEIOU'
    last_char = ''
    for char in reversed(word):
        if char in vowels:
            last_char = char
            break
    if last_char:
        index = len(word) - 1 - word[::-1].index(last_char)
        voice = word[:index + 1] + last_char * 3 + word[index + 1:]
    else:
        voice = word
    print(voice)
main(input())
