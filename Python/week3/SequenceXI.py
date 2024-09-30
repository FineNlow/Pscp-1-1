"""sequnceXI"""
def main():
    """process"""
    num = int(input())
    if num ==1:
        print("01")
    else:
        for i in range(1,(2*num)):
            for j in range(1,(2*num)):
                lowest = min(i,j,num,2*num-i,2*num-j)
                print(f"{lowest:02}",end = " ")
            print()
main()
