"""283"""
def train():
    """283"""
    start, stop = input().split(", ")
    p_s, p_d = "0", "0"
    while not p_s or not p_d:
        hua_kuy = input()
        if start == stop:
            print(0.00)
            break
        if hua_kuy == "Done":
            break
        f,l = hua_kuy.split(", ")
        if f == start:
            p_s = float(l)
        if f == stop:
            p_d = float(l)
    if p_s != "0" and p_d != "0":
        print(f"{(p_d - p_s):.2f}")
    else:
        print("Error")
train()
