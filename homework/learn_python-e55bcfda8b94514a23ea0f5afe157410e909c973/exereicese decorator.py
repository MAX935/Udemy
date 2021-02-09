 # Exereisece



def hello_from_decorator(origin_func):
    def wrap(*args,**kwargs):
        x = origin_func(*args, **kwargs)
        print(str(x) + ' Hello from decorator')
return wrap


@hello_from_decorator
def speak(x):
    return x

speak(input('Input some words'))