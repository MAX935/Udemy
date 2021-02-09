##def count(x):
##    i = 1
##    while i <= x:
##        yield i
##        i += 1
##
####
####x = count(8)
####print(x.__next__())
####print(x.__next__())
####print(x.__next__())
####print(x.__next__())
####print(x.__next__())
####print(x.__next__())
####print(x.__next__())
##
##a = count(10)
##a.__next__()
##a.__next__()
##
##a.__next__()
##a.__next__()
##
##
##
##
##for k in a:
##    print(k)
##
##def get_week_day():
##    i = 1
##    l ={1 : 'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7 :'Saturday'}
##    while i <= 7:
##        yield l[i]
##        i+=1
##
##
##current_day = get_week_day()
##print(current_day.__next__())
##print(current_day.__next__())
##print(current_day.__next__())
##print(current_day.__next__())
##print(current_day.__next__())
##print(current_day.__next__())
##print(current_day.__next__())
##
##def get_func():
##    week = [
##            "Sunday",
##            "Monday",
##            "Tuesday",
##            "Wednesday",
##            "Thursday",
##            "Friday",
##            "Saturday",
##        ]
##    for day in week:
##        yield day
##s = get_func()
##print(s.__next__())






##def even_odd():
##    word = 'even'
##    while 1:
##        yield word
##        if word == 'even':
##            word = 'odd'
##        else:
##            word = 'even'
##
##x = even_odd()
##print(x.__next__())
##print(x.__next__())
##print(x.__next__())
##print(x.__next__())
##print(x.__next__())

