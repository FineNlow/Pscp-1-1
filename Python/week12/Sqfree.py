"""Sqfree"""
def main(a):
    """Sqfree"""
    count = 0
    for i in range(1, a + 1):
        free = True
        for j in range(2, int(a**0.5) + 1):
            if j**2 > i:
                break
            if not i % (j**2):
                free = False
                break
        if free:
            count += 1
    print(count)
main(int(input()))
