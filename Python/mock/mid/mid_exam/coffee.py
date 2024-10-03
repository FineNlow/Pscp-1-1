"""coffee"""
def coffee():
    """coffee"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    pro1 = a + (e-1)*(a*((100-b)/100))
    pro2 = a * e
    if pro2 >= d:
        pro2 *= ((100-c)/100)
    if pro2 <= pro1:
        print("2")
        print(f"{pro2:.2f}")
    else:
        print("1")
        print(f"{pro1:.2f}")
coffee()
