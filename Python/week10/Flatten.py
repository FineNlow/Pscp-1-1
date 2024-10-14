"""Fart"""
import json
def flatten(lst):
    """Kyai"""
    if isinstance(lst, list):
        return sum([flatten(i) for i in lst], [])
    return [lst]
lst1 = json.loads(input())
flat_lst = flatten(lst1)
print(sorted(flat_lst, reverse=True))
