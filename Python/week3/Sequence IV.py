"""Sequence IV"""
def sequenceiv(n):
    """Sequence IV"""
    counter = 1
    for _ in range(n):
        line = ""
        for j in range(n):
            if j < n - 1:
                line += str(counter) + " "
            else:
                line += str(counter)
            counter += 1
        print(line)
sequenceiv(int(input()))
