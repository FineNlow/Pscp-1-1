"""Sequence VII"""
def main():
    """Bruh"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end =" ")
        print()
        if j == num:
            for a in range(num-1, 0 , -1):
                for b in range(1,a+1):
                    print(b, end = " ")
                print()
main()
