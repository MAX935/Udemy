# assert 2 + 2 == 6, 'mudak'

# def func(a,b):
#     assert b != 0, 'b musn\'t be equal zero'
#     return a / b
#
# print(func(12423,0))


# def multiply(a,b):
#     assert a > 0 and b > 0,'must be positive'
#     return a * b

# print(multiply(243,4242))


def passwords(password):
	pass_list = [1 , 2, 3, 4, 5]
	assert int(password) in pass_list,'pass in invalid'

passwords(6)