"""Taking turns"""
import json
def taking_turns():
    """Taking turns"""
    lst = json.loads(input())
    new = []
    l, r = 0, len(lst) - 1
    while l <= r:
        if r >= l:
            new.append(lst[r])
            r -= 1
        if l <= r:
            new.append(lst[l])
            l += 1
    print(new)
taking_turns()
