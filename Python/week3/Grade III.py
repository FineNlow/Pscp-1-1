"""Grade III"""
def grade(c):
    """Grade III"""
    count = 0
    for _ in range(1, c+1):
        total = float(input())
        match total:
            case total if 95 <= total <= 100:
                count += 4
            case total if 90 <= total < 95:
                count += 3.5
            case total if 85 <= total < 90:
                count += 3
            case total if 80 <= total < 85:
                count += 2.5
            case total if 75 <= total < 80:
                count += 2
            case total if 70 <= total < 75:
                count += 1.5
            case total if 65 <= total < 70:
                count += 1
            case total if 60 <= total < 65:
                count += 0.5
            case total if 0 <= total < 60:
                count += 0
    gradee = float(count / c) * 100
    gradee = int(gradee)
    print(f"{gradee/100:.2f}")
grade(int(input()))
