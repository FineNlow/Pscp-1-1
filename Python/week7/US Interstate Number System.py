"""US Interstate Number System"""
def interstate(num):
    """US Interstate Number System"""
    num_str = str(num)
    if 4 < num < 96:
        if num_str[-1] == "0":
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif num_str[-1] == "5":
            print("Vertical Major Interstate")
            print(f"I-{num}")
        else:
            print("Others")
    elif 99 < num < 1000:
        parent_interstate = int(num_str[1:3])
        first_digit = "Even" if not int(num_str[0]) % 2 else "Odd"
        if 4 < parent_interstate < 96:
            if not parent_interstate % 10:
                print(f"{first_digit} Minor Interstate")
                print(f"I-{parent_interstate}")
            elif parent_interstate % 10 == 5:
                print(f"{first_digit} Minor Interstate")
                print(f"I-{parent_interstate}")
            else:
                print("Others")
        else:
            print("Others")
    else:
        print("Others")
interstate(int(input()))
