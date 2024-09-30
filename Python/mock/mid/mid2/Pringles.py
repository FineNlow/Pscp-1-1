"""Pringles"""
def pringles():
    """Pringles"""
    u,m,d,l = input(),input(),input(),int(input())
    pick,count = "", 0
    for i in m:
        if l>0 and m == ")":
            count += 1
        else:
            pick += i
        l -= 1   
    print(count)
    print("There are still some left." if pick.count(")") > 0 else "None")
    print(u,m,d,sep="\n")    
pringles()
