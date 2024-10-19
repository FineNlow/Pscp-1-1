"""Socks"""
def socks():
    """Socks"""
    socks_lst = []
    socks_color = []
    socks_lst.extend(input())
    # แยกสี
    for color in socks_lst:
        if color not in socks_color:
            socks_color.append(color)
    socks_color.sort()
    result = []
    total_pairs = 0
    # หาคู่ ไม่มีก็ไม่เพิ่มเข้า list
    for i in socks_color:
        count = socks_lst.count(i)
        pairs = count // 2
        if pairs:  # ถ้ามีคู่
            result.extend([i * 2] * pairs)
            total_pairs += pairs
    if result:
        print(" ".join(result))
    else:
        print("None")
    print(total_pairs)
socks()
