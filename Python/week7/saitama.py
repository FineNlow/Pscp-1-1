"""saitama"""
from math import ceil
def find_most(x,y):
    """find max value"""
    if x > y:
        return x
    return y
def goal():
    "saitama training"
    g_push,g_sit,g_sd,g_run = int(input()),int(input()),int(input()),int(input())
    t_push,t_sit,t_run,t_sd = int(input()),int(input()),int(input()),int(input())
    total_push = ceil(g_push / t_push)
    total_sit = ceil(g_sit / t_sit)
    total_sd = ceil(g_sd / t_sd)
    total_run = ceil(g_run / t_run)
    findmost = find_most(total_run,find_most(total_sd,(find_most(total_push,total_sit))))
    print(findmost)
goal()
