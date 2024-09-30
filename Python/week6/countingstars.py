"""cs"""
def cs(text):
    """cs"""
    constellation = 0
    comet = 0
    shooting_star = 0
    con = ""
    for i in text:
        con += i
        if "~*" in con or "*~" in con:
            comet += 1
            con = ""
        elif "*/" in con:
            shooting_star += 1
            con = ""
        elif "**" in con:
            constellation += 1
            con = ""
        if con == " ":
            con = ""
    if not (constellation or comet or shooting_star):
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
cs(input())
