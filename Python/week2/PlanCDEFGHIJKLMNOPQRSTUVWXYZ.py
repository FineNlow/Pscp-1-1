"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if text == "Ascend":
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num1 > num2:
            num1, num2 = num2, num1
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
    elif text == "Descend":
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        if num1 < num2:
            num1, num2 = num2, num1
        print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
if __name__ == "__main__":
    main()
