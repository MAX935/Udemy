##def func(*args):
##    n = 1
##    for x in args:
##        n = n + x
##    return n
##
##z = func(5,6,7,8,9,2,4,5,6)
##print(z)


##def func(percent, *args):
##    result = 1
##    for x in args:
##        result = result * x
##    return result * percent / 100
##
##b = func(20,65,75,4)
##print(b)

##def mark(**kwargs):
##    if 'Audi' in kwargs:
##        print('Nice car, {}'.format(kwargs['Audi']))
##

##def hello(*args, **kwargs):
##    print(args)
##    print(kwargs)
##
##
##hello('Hello',1234,True, name = 'Maxim')

#1 задание

def is_cat_here(*args):
    l =[x.lower() for x in args]
    if 'cat' in l:
        return True
    else:
        return False

#2 задание

def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False

# 3 задание


def your_favourite_color(my_color, **kwargs):
    if 'color' in kwargs:
        if my_color in kwargs['color']:
            print('My favourite color is {}, what is your favourite color?'.format(my_color))
        else:
            print('My favourite color is {c},but {new} is also pretty good'.format(c = my_color, new = kwargs['color']))








