"""Again"""
def ps():
    """Kuy"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = input().strip()
    words = text.split()
    def count_vowels(word):
        return sum(1 for char in word.lower() if char in vowels)
    new = [word for word in words if count_vowels(word) >= 2]
    if new:
        new.sort()
        for word in new:
            print(word.replace(".",""))
    else:
        print("Nope")
ps()
