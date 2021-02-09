import time
from functools import wraps

def wait(sleep_time):
	def inner_func(orig_func):
		@wraps(orig_func)
		def wrap(*args, **kwargs):
			print('There was a pause {} seconds before execution {}'.format(sleep_time, orig_func.__name__))
			time.sleep(sleep_time)
			return orig_func(*args, **kwargs)
		return wrap
	return inner_func



@wait(5)
def test():
	pass


test()
