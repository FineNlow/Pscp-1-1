"""Program Triangle I"""
def triangle(a, b, c):
    """Func Triangle I"""
    if abs(a+b-c)<=0.01 or abs(a+c-b)<=0.01 or abs(b+c-a)<=0.01:
        print("Yes")
    else:
        print("No")
triangle(float(input())**2, float(input())**2, float(input())**2)
