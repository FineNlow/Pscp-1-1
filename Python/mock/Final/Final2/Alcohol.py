"""Alcohol"""
Gender_type = input()
Weight = float(input())
Cert = input()
Vol_can = float(input())
Vol_alc = float(input())
Ans = int(input())
Times = int(input())

Vol_alc_drink = (Vol_alc * Vol_can * Ans) / 100

def gender_cal(gender):
    """Calculated"""
    if gender == "Male":
        return (Vol_alc_drink / (Weight * 0.68 * 10)) * 1000
    if gender == "Female":
        return (Vol_alc_drink / (Weight * 0.55 * 10)) * 1000
    return 0

def alcohol():
    """Main"""
    gen_cal = gender_cal(Gender_type)
    r_gen_cal = gen_cal - (Times * 15)
    if r_gen_cal <= 50 and Cert == "Yes":
        print("Safe")
    else:
        print("Not Safe")
alcohol()
