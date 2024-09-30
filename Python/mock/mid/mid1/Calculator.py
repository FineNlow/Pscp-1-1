"""cal"""
def cal(num):
    """cal"""
    total = ""
    if num == 1:
        print(1)
    else:
        for i in range(1, num+1):
            if i < num:
                total += str(i)+"+"
            if i == num:
                total += str(i)+"="
        print(len(total))
cal(int(input()))
