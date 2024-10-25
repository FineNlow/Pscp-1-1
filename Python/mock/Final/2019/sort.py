"""sort"""
def rieang(lst):
    """bubble"""
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j + 1], lst[j]

def main():
    """main"""
    lst1 = []
    while True:
        num = input()
        if num == "END":
            break
        lst1.append(int(num))
    rieang(lst1)
    for i in lst1:
        print(i)
main()
