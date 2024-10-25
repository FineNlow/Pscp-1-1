"""Majority"""
def main(leader,people):
    """Majority"""
    votes = [0 for _ in range(leader)]
    max_score, winner = 0, 0
    for _ in range(people):
        vote = int(input())
        votes[vote-1] += 1
    for i in range(leader):
        if votes[i] > max_score:
            max_score = votes[i]
        if votes[i] >= people / 2:
            winner += i + 1
            break
    print(f"{winner} {max_score}" if winner else f"0 {max_score}")
main(int(input()), int(input()))
