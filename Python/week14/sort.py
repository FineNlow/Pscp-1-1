"""sort"""
def sort():
    """sorting"""
    num_lst = []
    while (num := input()) != "END":
        num_lst.append(int(num))
    for i in num_lst:
        if num_lst[i] > num_lst[i+1]:
            num_lst[i], num_lst[i+1] = num_lst[i+1], num_lst[i]
    print(*num_lst)
sort()
