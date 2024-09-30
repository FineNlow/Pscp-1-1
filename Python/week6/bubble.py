"""bubble"""
def big_bubble(indexes, cnt, path):#cnt -> นับว่ากระโดดกี่ครั้งแล้ว
    """calculate for big bubble(s)"""
    space_left = path.index("|") - indexes #อยู่ห่างกับเส้นชัยกี่ตำแหน่ง
    if space_left <= 3: #ถ้าบวกแล้วเกิน -> จบเลย
        return path.index("|"), cnt+1 #^O  | , index = 1, |'s index = 4
    for i in (3, 2, 1): # ^OooO|
        if "O" in path[indexes+1:indexes+4]: #O is first priortity ถ้ามีมาก่อน ยังไงก็ดีกว่า
            O_indexes = path.rfind("O", indexes+1, indexes+4)
            return O_indexes, cnt+1
        if path[indexes+i] != " ":
            return indexes + i, cnt+1 #ถ้าในระยะสามช่อง มีทางให้ไปเหยียบ -> ไป
    return indexes+1, cnt #ถ้าไปแล้วไม่มีทางให้เหยียบ
def bubble_spaces_finder(path):
    """find whether possible/impossibe to jump on the bubble"""
    indexes = 0 #o -> 1 step, O -> maximum 3 steps (or less)
    cnt = 1
    indexes += 1 #jump from the beginning point
    # impossible = False
    # possible = False
    while True:
        match path[indexes]:
            case "o":
                indexes += 1
                cnt += 1
            case "O":
                indexes, cnt = big_bubble(indexes, cnt, path)
        if path[indexes] == " ": #can't go more
            space_left = path.index("|") - (indexes - 1) #-1 means go back to old pos
            print("IMPOSSIBLE")
            print(space_left)
            break
            # impossible = True
        if path[indexes] == "|": #Wins
            print("POSSIBLE")
            print(cnt)
            break
            # possible = True
bubble_spaces_finder(input())
