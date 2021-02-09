#78
##
##
##import time
##
##start = time.time()
##x = sum([x for x in range(10000)])
##print('x_time = ', time.time() - start)
##
##start_y = time.time()
##y = sum(i for i in range(10000))
##print('y_time = ', time.time() - start_y)
##
##print(y)
##print(time.time())
import time
import functools

def time_count(origin_func):
    @functools.wraps(origin_func)
    def wrap(*args, **kwargs):
        time_start = time.time()
        origin_func(*args, **kwargs)
        time_of_performance = time.time() - time_start
        print('time = ', time_of_performance)
    return wrap

@time_count
def list_comprehension(x):
    l = sum([i for i in range(x)])



@time_count
def generator(x):
    m = sum(k for k in range(x))



list_comprehension(1000000)
generator(1000000)






