"""Restaurant"""
def res():
    """Restaurant"""
    a,b,c,d = float(input()),float(input()),float(input()),float(input())
    per = a*c
    ggg = a+d
    if ggg>b:
        print(f"No {float(per):.3f}")
    elif ggg<b:
        print(f"Yes {int(b*c):.3f}")
    else:
        print("Yes")
res()
