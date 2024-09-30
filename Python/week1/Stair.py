def min_steps_to_reach_top(y, n, heights):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        total_height = 0
        for j in range(i - 1, -1, -1):
            total_height += heights[j]
            if total_height > y:
                break
            dp[i] = min(dp[i], dp[j] + 1)

    return dp[n] if dp[n] != float('inf') else "NO"

y = int(input())
n = int(input())
heights = [int(input()) for _ in range(n)]

print(min_steps_to_reach_top(y, n, heights))
