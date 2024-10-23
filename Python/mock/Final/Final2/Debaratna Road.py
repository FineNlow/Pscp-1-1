"""Debaratna Road"""
def road(p_road):
    """Debaratna Road"""
    bangkok = 0 <= p_road < 5.033
    samut_prakarn = 5.032 < p_road < 35.478
    chachoengsao = 35.477 < p_road < 52.901
    chon_buri = 52.900 < p_road < 58.856
    invalid = p_road < 0 or p_road > 58.856
    roaddd = {bangkok: "Bangkok", samut_prakarn: "Samut Prakarn",chachoengsao: "Chachoengsao",
               chon_buri: "Chon Buri", invalid: "InValid"}
    print(roaddd[True in roaddd])
road(float(input()))
