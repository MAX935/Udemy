##def find_car():
##    print('car was founded')

##def decorated_func(orig_func):
##    def wraped_func():
##        print('wraped func was called')
##        orig_func()
##        print('Orig function was implemented')
##    return wraped_func
##
####decor_func = decorated_func(find_car)
####decor_func()
##
##
##
##decorated_func
##def simple_func():
##    print('simple function')
##
##simple_func()
##
##
##simple_func()



###Декоратор с args**
##def decorator_function(orig_function):
##    def wraped_func(*args):
##        print('OO! You bye a new car!!!!\n Yes!! It\'s ')
##        orig_function(*args)
##        print('Great!!!!')
##    return wraped_func
##
##
##@decorator_function
##
##def simple_func(*args):
##
##    l = [i for i in args]
##    for g in l:
##        print(g)
##
##
##x = input('Brand of the car: ')
##k = input('Brand of the car: ')
##z = input('Brand of the car: ')




#Декоратор с **kwargs

def decorator_function(orig_function):
    def wraped_func(**kwargs):
        print('OO! You bye a new car!!!!\n Yes!! It\'s ')
        orig_function(**kwargs)
        print('Great!!!!')
    return wraped_func


@decorator_function


def simple_func(**kwargs):
    print(kwargs)
simple_func(Audi='A4', BMW=5,Mercedes='E200')




