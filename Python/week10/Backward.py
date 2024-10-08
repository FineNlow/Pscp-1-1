"""Backward"""
def main():
    """Backward"""
    rvs_lst = []
    while (inrev := input()) != 'NULL':
        rvs_lst.append(inrev)
    print(*reversed(rvs_lst),sep="\n")
main()
