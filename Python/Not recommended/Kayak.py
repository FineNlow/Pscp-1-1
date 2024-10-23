"""Kayak"""
n = int(input())
weights = list(map(int, input().split()))
weights.sort()
min_diff = float('inf')
for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        remaining_weights = []
        for k in range(2 * n):
            if k != i and k != j:
                remaining_weights.append(weights[k])
        total_difference = 0
        for k in range(1, len(remaining_weights), 2):
            total_difference += remaining_weights[k] - remaining_weights[k - 1]
        min_diff = min(min_diff, total_difference)
print(min_diff)
