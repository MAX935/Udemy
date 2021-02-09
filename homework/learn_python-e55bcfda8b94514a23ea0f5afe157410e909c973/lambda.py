#MAP
##
##def func(x):
##    return x + x
##
##
##x = [1, 2, 5, 6, 7, 45, 5435, 345346, 6363, 43645, 6345]
##
##
##l = list(map(func, x))
##print(l)



##def find(car):
##    if 'A3' in car:
##        print('A3 was founded!')
##        return True
##    else:
##        print('A3 was not founded!')
##        return False
##
##
##cars_list = ['A1', 'A3','A4','A7']
##
##x = list(map(find, cars_list))
##print(x)


#Filter


##def odd(x):
##    return x % 2 == 0
##
##x = [1, 10, 24, 1234,534566, 534645,6,355345,534643,42353,423,1231,23,5,6,7,8,9]
##
##
##x =list(filter(odd,x))
##print(x)
##


#lambda expression



l = [1, 10, 24, 1234,534566, 534645,6,355345,534643,42353,423,1231,23,5,6,7,8,9]
q = list(map(lambda x: x ** 3,l))
print(q)






