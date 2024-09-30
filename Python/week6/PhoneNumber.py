"""PhoneNumber"""
def phonenumber(p_num, nation):
    """PhoneNumber"""
    if nation == "Domestic":
        for i in range(p_num):
            if not len(str(i)) == 9:
                print(i[0] + " " + i[1:5] + " " + i[6:8] )
phonenumber(int(input), input())
