"""PickThem"""
import json
def pt():
    """PickThem"""
    lst = []
    for i in json.loads(input()):
        if not i % 2:
            lst.append(i)
    if not lst:
        print("Nope")
    else:
        for j in lst:
            print(j)
pt()
