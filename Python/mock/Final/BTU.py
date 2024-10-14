"""BTU"""
def btu():
    """BTU"""
    ft = int(input())
    height = int(input())
    human_num = int(input())
    room = input()
    sun = input()
    btuu = 0
    one = 99 < ft <= 150
    two = 150 < ft <= 250
    three = 250 < ft <= 300
    four = 300 < ft <= 350
    five = 350 < ft <= 400
    six = 400 < ft <= 450
    seven = 450 < ft <= 550
    eight = 550 < ft <= 700
    nine = 700 < ft <= 1000
    ten = 1000 < ft <= 1200
    eleven = 1200 < ft <= 1400
    twelve = 1400 < ft <= 1500
    thirteen = 1500 < ft <= 2000
    fourteen = 2000 < ft <= 2500
    chk = {one : 5000, two : 6000, three : 7000, four : 8000, five : 9000
    , six : 10000, seven : 12000, eight : 14000, nine : 18000, ten : 21000
    , eleven : 23000, twelve : 24000, thirteen : 30000, fourteen : 34000}
    for con,value in chk.items():
        if con:
            btuu += value
    if height > 8:
        height_out = height - 8
        btuu += height_out * 1000
    if human_num > 2:
        human_num_out = human_num - 2
        btuu += human_num_out * 600
    if room != "Normal":
        btuu += 4000
    if sun != "Normal":
        if sun == "shaded":
            btuu -= btuu * 0.1
        elif sun == "facing the sun":
            btuu += btuu * 0.1
    print(int(btuu))
btu()
