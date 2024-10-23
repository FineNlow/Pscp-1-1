"""Stuttering"""
def auang():
    """Stuttering"""
    word = input().split()
    real = []
    for words in word:
        if not real or real[-1] != words:
            real.append(words)
    print(*real)
auang()
