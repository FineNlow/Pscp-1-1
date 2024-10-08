"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def ps():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    bowel = ['a','e','i','o','u']
    lst = [input().split(" ")]
    count_bowel = []
    for i in lst:
        count = 0
        for char in len(i):
            if i in bowel:
                count += 1
        count_bowel.append(count)
    
ps()
