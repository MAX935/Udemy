def func(n, f_second):
    x = 1
    for i in range(1,n):
        x *= f_second(i)
    return x

def f_second(t):
    return t * t



def cube(t):
    return t ** 3



x = func(3, cube)
print(x)