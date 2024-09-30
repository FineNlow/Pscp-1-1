"""SequenceIX"""
def seq(num):
    """SequenceIX"""
    count = num-1
    for i in range(num):
        print(" "*(3*count) ,end = " ")
        count -= 1
        for j in range(1,i+2):
            print(f"{j:02}" , end= " ")
        for j in range(j-1,0,-1):
            print(f"{j:02}" , end= " ")
        print()
seq(int(input()))
