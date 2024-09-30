"""elo musk"""
def elo(ra,rb,team):
    """elo"""
    ea = 1 / (1 + 10 ** ((rb - ra) / 400))
    eb = 1 / (1 + 10 ** ((ra - rb) / 400))
    print(f"{ea:.2f}" if team == "A" else f"{eb:.2f}")
elo(int(input()),int(input()),input())
