"""WPM"""
def kid(wpm):
    """Kid"""
    very_slow = wpm < 11
    slow = 11 <= wpm < 21
    avg = 21 <= wpm < 31
    fast = 31 <= wpm <= 40
    very_fast = wpm > 40
    chk = {very_slow: "Very Slow", slow: "Slow", avg: "Average", fast: "Fast", \
           very_fast: "Very Fast"}
    return chk[True in chk]

def adult(wpm):
    """Adult"""
    very_slow = wpm < 26
    slow_begin = 26 <= wpm < 36
    avg_inter = 36 <= wpm < 46
    fast_adv = 46 <= wpm < 66
    very_fast = 66 <= wpm <= 80
    insane = wpm > 80
    chk = {very_slow: "Very Slow", slow_begin: "Slow/Beginner", avg_inter: "Intermediate/Average", \
           fast_adv: "Fast/Advanced", very_fast: "Very Fast", insane: "Insane"}
    return chk[True in chk]

def main(gen, wpm1):
    """main"""
    print(kid(wpm1) if gen == "Kids" else adult(wpm1))
main(input(),int(input()))
