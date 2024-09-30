"""SurprisingVote"""
def surpirsing(x, y):
    """SurprisingVote"""
    result = y - max(0,x - y*2)
    if result <= 2:
        print("Not surprising")
    else:
        print("Surprising")
surpirsing(float(input()), float(input()))
