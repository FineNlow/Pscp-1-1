"""PrasomSib"""
def main(num_str):
    """PrasomSib"""
    count = 0
    num = [int(n) for n in num_str]
    for i in range(len(num)):
        plus = 0
        for j in range(i, len(num)):
            plus += num[j]
            if plus == 10:
                count += 1
    print(count)
main(input())
