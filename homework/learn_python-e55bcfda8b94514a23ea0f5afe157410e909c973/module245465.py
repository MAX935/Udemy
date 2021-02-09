def calc(n,func):
    result = 0
    for i in range(1,n):
        result *= func(n)
    return result

def func(m):
    return m ** 2


