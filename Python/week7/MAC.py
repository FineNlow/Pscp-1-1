"""MAC"""
def mac(address):
    """MAC"""
    mac_text = "ABCDEFabcdef0123456789-:."
    check = True
    if len(address) >= 17:
        valid1 = address[2] == "-" and address[5] == "-" and address[8] == "-" \
        and address[11]=="-" and address[14]=="-" and len(address)==17 and address.count("-")==5

        valid2 = address[2] == ":" and address[5] == ":" and address[8] == ":" \
        and address[11]==":" and address[14]==":" and len(address)==17 and address.count(":")==5
    else:
        valid1 = valid2 = False

    if len(address) >= 14:
        valid3 = address[4] == "." and address[9] == "." and len(address) == 14 \
        and address.count(".") == 2 and address[:4].isalnum() and address[5:9].isalnum() \
        and address[10:].isalnum()
    else:
        valid3 = False

    for i in address:
        if i not in mac_text:
            check = False
            break
    if not (len(address) == 14 or len(address) == 17):
        check = False
    if check and (valid1 or valid2 or valid3):
        if valid1:
            print("VALID 1")
        elif valid2:
            print("VALID 2")
        elif valid3:
            print("VALID 3")
    else:
        print("ERROR")
mac(input())
