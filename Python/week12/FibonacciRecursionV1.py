"""FibonacciRecursionV1"""
def fibo(n):
    """fibo"""
    if not n:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
n1 = int(input())
print(fibo(n1))
