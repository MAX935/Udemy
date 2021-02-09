##def sew_machine():
##    max_count = 190
##    patterns = ['x', 'o', '*', '%']
##    result_map = []
##
##    i = 0
##
##    while len(result_map) <= max_count:
##        if i >= len(patterns):
##            i = 0
##        result_map.append(patterns[i])
##        i+=1
##    return result_map
##
##x = sew_machine()
##print(x)
##
##
##
##
##
##
##
##def sew_machine2():
##    max_count = 190
##    patterns = ['x', 'o', '*', '%']
##    result_map = []
##
##    for i in range(max_count):
##         if i >= len(patterns):
##            i = 0
##    result_map.append(patterns[i])
##
##
##    return result_map
##
##x = sew_machine2()
##print(x)

##
##def gen_sew_machine():
##    patterns = ('x', 'o','*', '%')
##    i = 0
##    while True:
##        if i >= len(patterns):
##            i = 0
##        yield patterns[i]
##        i+=1
##
##
##x = gen_sew_machine()
##print(x.__next__())
##print(x.__next__())
##print(x.__next__())
##print(x.__next__())
##


def pow_calc():
    i = 1
    while 1:
        yield i ** 2
        i+=1


x = pow_calc()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
