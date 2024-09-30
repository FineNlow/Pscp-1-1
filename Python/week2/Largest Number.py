"""Largest Number"""
def main(a,b,c):
    """Process"""
    num1 = a + b + c
    num2 = a + c + b
    num3 = b + a + c
    num4 = b + c + a
    num5 = c + b + a
    num6 = c + a + b
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    num5 = int(num5)
    num6 = int(num6)
    highest =  num1
    if num2 > highest:
        highest = num2
    if num3 > highest:
        highest = num3
    if num4 > highest:
        highest = num4
    if num5 > highest:
        highest = num5
    if num6 > highest:
        highest = num6
    print(highest)
main(input(),input(),input())
