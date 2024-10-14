"""FIboV2"""
MEMO = {0: 0, 1: 1}
def fibov2(n):
    """Memo"""
    if n in MEMO:
        return MEMO[n]
    value = fibov2(n - 1) + fibov2(n - 2)
    MEMO[n] = value
    return value
def cal_fib(start,stop):
    """Manual loop"""
    if start > stop:
        return []
    result = []
    return result + cal_fib(start + 1,stop)
def size_fib(start,stop,size):
    """limit batch sizing"""
    if start > stop:
        return []
    result = cal_fib(start, min(start + size -1, stop))
    return result + size_fib(start + size, stop, size)
def main():
    """main"""
    n1 = int(input())
    size = 980
    results = size_fib(0, n1, size)
    print(results[-1])
main()
