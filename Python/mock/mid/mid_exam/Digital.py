"""Digital"""
def check():
    """Digital"""
    name = input()
    nationality = input()
    home = input()
    age = float(input())
    salary = float(input())
    in_money = float(input())
    chk_True = nationality in ("Yes","True") and home in ("Yes","True")
    if chk_True and age >= 16 and salary <= 840000 and in_money <= 500000:
        print(f"Congratulations! {name} is qualified to receive a digital wallet amount\
of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
check()
