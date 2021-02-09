# def dec_val(value):
#     def dec_func(original_func):
#         def wrap(*args, **kwargs):
#             if args and args[0] != value:
#                 print('First value should be {}'.format(value))
#             return original_func(*args, **kwargs)
#         return wrap
#     return dec_func
#
#
# @dec_val('two')
# def imp_func(*args, **kwargs):
#     print(args, kwargs)
#
#
# imp_func('one','two','three', key=127)
#
#

def enforce(*types):
    print(types)
    def inner_dec(orig_func):
        def wrap(*args, **kwargs):
            new_args = []
            for i,k in zip(args,types):
                print(i,k)
                new_args.append(k(i))
            print(new_args)
            return orig_func(*new_args, **kwargs)
        return wrap
    return inner_dec

@enforce(str,int)
def print_text_in_time(text, n):
    for n in range(n):
        print(text)

print_text_in_time('Hello', '5')
