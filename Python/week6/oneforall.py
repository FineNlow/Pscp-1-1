"""oneforall"""
def allm(gen):
    """beaw"""
    count = 1
    nnn = ""
    for i in range(gen):
        name=input()
        if not i%2 and count!=gen:
            nnn += name+("*"*count)
        elif i%2 and count!=gen:
            nnn += name+("-"*count)
        count+=1
        if i==gen-1:
            nnn += f"{name}_{gen}"
    print(nnn)
allm(int(input()))
