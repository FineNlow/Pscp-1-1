"""Century"""
def years(n_year):
    """Cen"""
    for _ in range(n_year):
        bead = input()
        prefix = bead[:5]
        input_y = int(bead[5:])
        if prefix == "B.E.":
            if input_y < 544:
                print("ERROR")
            else:
                input_y -= 543
                print(input_y // 100)
        elif prefix == "A.D.":
            print(input_y // 100)
        else:
            print("ERROR")
years(int(input()))
