"""Sequence X"""
def main():
    """Sequence X"""
    num = int(input())
    count = num-1
    for i in range(1,num+1):
        print(" "*(count*3) ,end = "")
        count -= 1
        for j in range(1,i+1):
            print(f"{j:02}" , end = " ")
        for j in range(i-1,0,-1):
            print(f"{j:02}" , end = " ")
        print()
    count = 0
    for i in range(num-1 ,0,-1):
        count += 1
        print(" "*(3*count) ,end = "")
        for j in range(1,i+1):
            print(f"{j:02}" , end = " ")
        for j in range(i-1,0,-1):
            print(f"{j:02}" , end = " ")
        print()
main()
