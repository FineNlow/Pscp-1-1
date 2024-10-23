"""BloodDonation"""
def can_donate_blood(age, weight, donation_count):
    """EIEI"""
    chk_age = 17 <= age <= 70
    chk_w = weight >= 45
    chk_d = age <= 55 if not donation_count else True
    chk_four = age == 17 or 60 <= age <=  70
    if chk_age:
        if chk_four:
            med_ver = input()
            if chk_w and chk_d:
                print("Yes" if med_ver == "True" else "No")
            else:
                print("No")
        elif chk_w and chk_d:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
can_donate_blood(int(input()), int(input()), int(input()))
