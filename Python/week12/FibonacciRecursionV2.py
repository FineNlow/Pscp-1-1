"""Rev2"""
fibo_cache = {0: 0, 1: 1}
def fibo(num):
    """fibo"""
    if num in fibo_cache:
        return fibo_cache[num]
    fibo_cache[num] = fibo(num - 1) + fibo(num - 2)
    return fibo_cache[num]
def batch_fib(start, end, batch_size):
    """loop setting batch size"""
    if start > end:
        return []
    return calculate_fib(start, min(start + batch_size - 1, end)) + \
    batch_fib(start + batch_size, end, batch_size)
def calculate_fib(start, end):
    """first loop"""
    if start > end:
        return []
    return [fibo(start)] + calculate_fib(start + 1, end)
def ans():
    """main"""
    num = int(input())
    print(batch_fib(0, num, 980)[-1])
ans()
