import functools


def decorator_func(orig_func):
    """
    Decorator function documentation!!!
    """

    @functools.wraps(orig_func)
    def wrapped(*args, **kwargs):
        print('You are using function bla bla bla')
        print('{}'.format(orig_func.__doc__))
        print(orig_func.__name__)
        #return orig_func(*args, **kwargs)
    return wrapped






@decorator_func
def calc(a, b):
    """
    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers

    """
    return a ** 2 + b ** 2


calc(2,5)

#documentation of decorator

print(calc.__doc__)
print(calc.__name__)
