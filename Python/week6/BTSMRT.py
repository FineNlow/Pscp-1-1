"""BTSMRT"""
def skytrain(days, age, height):
    """BTSMRT function"""
    if days == "Senior Day":
        if age >= 60:
            print("FREE")
        elif age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
    elif days == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        else:
            print("PAY")
    elif days == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
skytrain(input(), float(input()), float(input()))
