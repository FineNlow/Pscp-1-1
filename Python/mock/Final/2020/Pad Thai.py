"""Pad Thai"""
def main():
    """Rest"""
    ingredients = [
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", 
        "Bean Sprouts", "Noodle", "Chives", "Lime", 
        "Egg", "Oil", "Peanuts"
    ]
    flavors = ["Sweet", "Sour", "Salty"]
    used_ingredients = []
    used_flavors = []
    chk_in = True
    chk_fla = True
    while True:
        ing = input()
        if ing == "Cook":
            break
        if ing not in ingredients:
            chk_in = False
        used_ingredients.append(ing)
    while True:
        rod = input()
        if rod == "End":
            break
        if rod not in flavors:
            chk_fla = False
        used_flavors.append(rod)
    if len(set(used_ingredients)) < 11:
        print("This is bad!")
    elif len(set(used_ingredients)) == 11 and (len(set(used_flavors)) != 3 or not chk_fla):
        print("Not Bad...")
    elif not chk_in:
        print("This is not Pad Thai!!!")
    else:
        print("Delicious!")
main()
