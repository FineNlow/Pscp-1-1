"""Sequence VIII"""
def main():
    """Sequence VIII"""
    num = int(input())
    count = num-1
    for i in range(num):
        print(" "*(3*count) ,end = "")
        count -= 1
        for j in range(1,i+2):
            print(f"{j:02}" , end =" ")
        print()
main()
