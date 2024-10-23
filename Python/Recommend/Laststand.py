"""Laststand"""
from json import loads
def ls():
    """Retry"""
    lst = loads(input())
    for last in lst:
        print(str(last)[-1])
ls()
