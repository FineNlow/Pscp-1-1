"""T-score"""
def score(n,_):
    """T-score"""
    student_scores = [int(input()) for _ in range(n)]
    avg = sum(student_scores) / n
    sum_x2 = sum(score**2 for score in student_scores)
    sd = ((n * sum_x2 - (sum(student_scores) ** 2)) / (n * (n - 1))) ** 0.5
    t_scores = [50 + (10 * (scr - avg) / sd) for scr in student_scores]
    for scorer in t_scores:
        print(f"{scorer:.2f}")
score(int(input()), int(input()))
