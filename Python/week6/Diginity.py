"""Diginity"""
def main(zzz):
    """kwai"""
    while zzz != "0":
        if len(zzz) >= 2:
            total = 0
            while len(zzz) > 1:
                total = 0
                for i in zzz:
                    total += int(i)
                zzz = str(total)
        print(zzz)
        zzz = input()
main(input())
