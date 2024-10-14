"""Kyai"""
def main():
    """Kyai"""
    menu = []
    while True:
        menu_input = input()
        if menu_input == "DONE":
            break
        if menu_input == "CLOSED":
            menu.clear()
            break
        if menu_input == "SOMETHING'S WRONG":
            menu.clear()
            continue
        if menu_input.startswith("Can't do: "):
            menu_name = menu_input.lstrip("Can't do: ")
            menu.remove(menu_name)
        else:
            menu_cost = menu_input.split(" #")
            if menu_cost[1] == "N":
                menu.append(menu_cost[0])
            else:
                menu.insert(int(menu_cost[1]) - 1, menu_cost[0])
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
main()
