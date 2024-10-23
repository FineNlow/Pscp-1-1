"""Imposter"""
def imp():
    """Imposter"""
    among = {}
    voted = []
    dead = {}
    impostor_count = 0
    # crews input
    while True:
        name = input()
        if name == "Start":
            break
        us = name.replace("{","").replace("}","").replace('"', '')
        crew, role = us.split(" : ")
        among[crew] = role
    # Dead
    while True:
        vote_out = input()
        if vote_out == "End":
            break
        voted.append(vote_out)
    # vote
    for name, role in list(among.items()):
        if name in voted:
            dead[name] = role
            del among[name]
        elif role == "Impostor":
            impostor_count += 1
    # result
    print(f"{impostor_count} Impostor Remains\n***Alive***")
    for name, role in sorted(among.items()):
        print(f"{name} : {role}")
    print("***Dead***")
    for name, role in sorted(dead.items()):
        print(f"{name} : {role}")
imp()
