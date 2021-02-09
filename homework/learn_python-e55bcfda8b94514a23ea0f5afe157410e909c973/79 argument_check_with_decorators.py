##def prohibite_kwargs(orig_func):
##    def wrap(*args, **kwargs):
##        if kwargs:
##            raise ValueError('Kwargs are prohibited')
##        return orig_func(*args,**kwargs)
##    return wrap
##
##@prohibite_kwargs
##def func(*args, **kwargs):
##    print('It works')
##
##func(12)



def prohibit_more_than_2_arguments(orig_func):
    def wrap(*args, **kwargs):
        if len(args) > 2:
            raise ValueError('Function must have less than 3 arguments')
        return orig_func(*args, **kwargs)
    return wrap



@prohibit_more_than_2_arguments
def func(*args, **kwargs):
    print(args, kwargs)



