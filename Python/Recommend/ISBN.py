"""ISBN"""
def isbn(code):
    """โจทย์ซะยาว แก่นมึงมีแค่สูตร ไอสลัดผัก🤡"""
    x = 0
    mm = 10
    for num in code[:10]:
        if mm != 1:
            x += mm * int(num)
            mm -= 1
        else:
            break
    chk = "X" if -x%11 == 10 else str(-x%11)
    print("Yes" if chk == code[-1] else f"No {chk}")
isbn(input().replace("-",""))
