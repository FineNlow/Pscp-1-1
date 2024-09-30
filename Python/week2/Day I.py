"""Lab"""
def years(x):
    """Lab"""
    if not x % 4:
        if not x % 100:
            if not x % 400:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
years(int(input()))
