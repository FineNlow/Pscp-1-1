"""Blackjack"""
def bj(num):
    """Retired"""
    score, ace = 0, 0
    for _ in range(num):
        card = input()
        if card.isnumeric():
            score += int(card)
        else:
            if card == "A":
                if ace == 1:
                    score += 1
                    continue
                score,ace = score+11,ace+1
            else:
                score += 10
    while score > 21 and ace == 1:
        score, ace = score-10,ace-1
    print(score)
bj(int(input()))
