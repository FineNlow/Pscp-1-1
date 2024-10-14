"""Difference"""
def main(n,m):
    """Difference"""
    sta = set(int(input()) for _ in range(n))
    stb = set(int(input()) for _ in range(m))
    print(*sorted(sta.difference(stb)))
main(int(input()),int(input()))
