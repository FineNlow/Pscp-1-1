"""meow"""
def main():
    """ee"""
    for _ in range(10):
        zzz=input()
        total=0
        for i in zzz:
            if i.isnumeric():
                total+=int(i)
        if not total or not int(zzz):
            print("No")
        elif not int(zzz)%total:
            print("Yes")
        else:
            print("No")
main()
