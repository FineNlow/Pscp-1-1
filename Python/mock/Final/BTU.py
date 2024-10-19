"""BTU"""
def btu1(ft):
    """BTU"""
    one = 99 < ft <= 150
    two = 150 < ft <= 250
    three = 250 < ft <= 300
    four = 300 < ft <= 350
    five = 350 < ft <= 400
    six = 400 < ft <= 450
    seven = 450 < ft <= 550
    chk = {one : 5000, two : 6000, three : 7000, four : 8000, five : 9000,
           six : 10000, seven : 12000}
    return chk[True]
def btu2(ft):
    """BTU2"""
    eight = 550 < ft <= 700
    nine = 700 < ft <= 1000
    ten = 1000 < ft <= 1200
    eleven = 1200 < ft <= 1400
    twelve = 1400 < ft <= 1500
    thirteen = 1500 < ft <= 2000
    fourteen = 2000 < ft <= 2500
    chk = {eight : 14000, nine : 18000, ten : 21000, eleven : 23000,
           twelve : 24000, thirteen : 30000, fourteen : 34000}
    return chk[True]
def main(ft1, height, human_num, room, sun):
    btuu = btu1(ft1) if ft1 < 551 else btu2(ft1)
    chk_height = height > 8
    chk_human = human_num > 2
    chk_room = room == "kitchen"
    chk_n_sun = sun == "Normal"
    chk_s_sun = sun == "shaded"
    chk_f_sun = sun == "facing the sun"
    chk = {
        chk_height: (height - 8) * 1000,
        chk_human: (human_num - 2) * 600,
        chk_room: 4000,
        chk_n_sun: 0,
        chk_f_sun: btuu * 0.1,
        chk_s_sun: -(btuu * 0.1)
    }
    btuu += chk[chk_height] + chk[chk_human] + chk[chk_room] + chk[chk_n_sun] + chk[chk_f_sun] + chk[chk_s_sun]
    print(int(btuu))
main(int(input()),int(input()),int(input()),input(),input())
