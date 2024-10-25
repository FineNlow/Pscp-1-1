"""ATM"""
def atm(bank):
    """atm"""
    while (put := input()) != "END":
        if put[0] == "D":
            bank += int(put[2::])
        elif put[0] == "W":
            if bank < int(put[2::]):
                bank = 0
                continue
            bank -= int(put[2::])
    print(bank)
atm(int(input()))
