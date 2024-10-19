"""Cat fuck Fox"""
def main():
    """Cat Fox count and sort"""
    fox, cat = 0, 0
    ani_dct = {}
    cat_dct, fox_dct = {}, {}
    for _ in range(int(input())):
        animal = input().replace("{", "").replace("}", "")
        name, position = animal.split(" : ")
        name = name[1:-1]
        position = position[1:-1]
        ani_dct.update({name: position})
    for key, value in ani_dct.items():
        if value[:3] == "Cat":
            cat += 1
            cat_dct[key] = value
        elif value[:3] == "Fox":
            fox += 1
            fox_dct[key] = value
    if 'Cat01' not in cat_dct.values():
        cat_dct.update({'Garfield': 'Cat01'})
        cat += 1
    if 'Fox01' not in fox_dct.values():
        fox_dct.update({'Fubuki': 'Fox01'})
        fox += 1
    print(f"Cat : {cat}")
    print(f"Fox : {fox}")
    def get_number(s):
        return int(s[3:])
    for key, value in sorted(cat_dct.items(), key=lambda item: get_number(item[1])):
        print(f"{key} : {value}")
    for key, value in sorted(fox_dct.items(), key=lambda item: get_number(item[1])):
        print(f"{key} : {value}")
main()
