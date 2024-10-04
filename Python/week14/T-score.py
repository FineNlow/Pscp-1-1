"""ttt"""
def main():
    """T-Score"""
    for _ in range(n):
        
def find_total():
    """find total"""
    total = 0
    for _ in range(n):
        total += int(input())
    return total
def xbar():
    """xbar"""
    xbar = find_total() / n
    return xbar
def sd():
    """s"""
    sd = ((n*(find_total()**2)) - (find_total()**2)) / n*(n-1)
    return sd
def z():
    """z"""
    z = (find_total() - xbar()) / sd()
def tscore():
    """T-Score"""
    tscore = 50 + (10*z())
    return tscore

n = int(input())
