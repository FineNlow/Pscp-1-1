"""Big frame"""
def bf():
    """Big frame"""
    line1 = input().strip()
    line2 = input().strip()
    line3 = input().strip()
    line4 = input().strip()
    line5 = input().strip()
    max_length = max(len(line1), len(line2), len(line3), len(line4), len(line5))
    print('*' * (max_length + 4))
    print(f"* {line1.ljust(max_length)} *")
    print(f"* {line2.ljust(max_length)} *")
    print(f"* {line3.ljust(max_length)} *")
    print(f"* {line4.ljust(max_length)} *")
    print(f"* {line5.ljust(max_length)} *")
    print('*' * (max_length + 4))
bf()
