"""SequnceXII"""
def main(num):
    """Piece of last sh*t"""
    for i in range(-num+1,num):
        for j in range(-num+1,num):
            ans = num-abs(abs(i)-abs(j))
            print(f"{ans:02}" ,end =" ")
        print()
main(int(input()))
