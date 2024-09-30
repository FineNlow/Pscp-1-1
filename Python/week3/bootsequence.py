"""boot"""
def boot(n):
    """boot"""
    result = ""
    for i in range(1, n + 1):
        if i < n:
            result += str(i) + "_"
        else:
            result += str(i)
    print(result)
boot(int(input()))
