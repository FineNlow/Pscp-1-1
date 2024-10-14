"""Ez"""
def main():
    """Ez"""
    lst = []
    lst.extend(input().replace(" ", ""))
    sort_lst = sorted(lst, key=lambda s: (s.lower(), s.isupper()))
    unique_lst = sorted(set(sort_lst), key=lambda s: (s.lower(), s.isupper()))
    def c_lst(cc, lst):
        """นับ"""
        total = 0
        for i in lst:
            if i == cc:
                total += 1
        return total
    for i in unique_lst:
        if i.isalpha():
            print(f"{i} = {c_lst(i, lst)}")
main()
