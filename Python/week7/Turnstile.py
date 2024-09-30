"""Turnstile"""
def turnstile():
    """Turnstile"""
    state = "Locked"
    people_through = 0
    while (action := input()) != "END":
        if state == "Locked" and action == "C":
            state = "Unlocked"
        elif state == "Unlocked" and action == "P":
            state = "Locked"
            people_through += 1
    print(people_through)
turnstile()
