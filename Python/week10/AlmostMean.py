"""AlmostMean"""
def main(n):
    """AlmostMean"""
    students = [input().split('\t') for _ in range(n)]
    students = [(sid, float(score)) for sid, score in students]
    avg = sum(score for _, score in students) / n
    result = max((s for s in students if s[1] <= avg), key=lambda x: x[1])
    print(f"{result[0]}\t{result[1]}")
main(int(input()))
