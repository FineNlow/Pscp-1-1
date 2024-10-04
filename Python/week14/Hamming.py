"""Hamming"""
def ham(message1, message2):
    """Hamming"""
    count = 0
    for i, _ in enumerate(message1):
        if message1[i] != message2[i]:
            count += 1
    print(count)
ham(input(), input())
