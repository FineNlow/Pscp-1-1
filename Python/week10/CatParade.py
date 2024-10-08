def catparade():
    """kitty"""
    ani_lst = []
    ani_count_position = {}
    #input
    while (animals := input()) != "END":
        animals = animals.split(",")
        for ani in animals:
            if ani == "IT'S A DOG" and ani_lst:
                ani_lst.pop()
            else:
                ani_lst.append(ani)
    #position
    for i, ani in enumerate(ani_lst):
        if ani not in ani_count_position:
            ani_count_position[ani] = i+1
    #count
    ani_lst = ani_lst.sort()
    for anis in enumerate(ani_lst):
        count = 0
        if anis == ani_lst[i]:
            count += 1
        else:
            count = 0

catparade()
