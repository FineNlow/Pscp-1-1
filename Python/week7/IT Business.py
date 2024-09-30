"""IT Business"""
def buss(bank, cash):
    """IT Business"""
    fail_attempts = 0
    input_statement = ""
    while input_statement != "end":
        input_statement = input()
        dow = input_statement[0]
        if dow == "D" and float(input_statement[2:]) <= cash:
            cash -= float(input_statement[2:])
            bank += float(input_statement[2:])
            fail_attempts = 0
        elif dow == "W" and float(input_statement[2:]) <= bank:
            cash += float(input_statement[2:])
            bank -= float(input_statement[2:])
            fail_attempts = 0
        else:
            fail_attempts += 1
        if fail_attempts == 3:
            break
    print(f"{bank:.2f}")
    print(f"{cash:.2f}")
buss(float(input()), float(input()))
