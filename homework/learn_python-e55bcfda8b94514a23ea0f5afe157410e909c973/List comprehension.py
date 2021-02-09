#
# # str = 'gdfgfdfgfdgdfdqweqeqwzcxczx'
# # l = []
# #
# # for i in str:
# #     l.append(i)
# # print('l = ', l)
#
#
#
# # str = 'gdfgfdfgfdgdfdqweqeqwzcxczx'
# #
# # new_list =[i for i in str]
# # print(new_list)
# #
# #
# # dict = {1:'one', 2: 'two'}
# # dict_values = [values for values in dict.values()]
# # print(dict_values)
#
#
#
# from random import randint
# list_rand = []
# for i in range(-15,15):
#     list_rand.append(randint(-100,100))
# print(list_rand)
#
# positive = [x for x in list_rand if x > 0]
# print(positive)
#
# h = ['+' if n > 0 else '-' for n in list_rand]
# print(h)



greetings = ['hello', 'hi', 'hey', 'hola']
p = []
for i in greetings:
    p.append(list(i)[1])
print(p)

p2 = [list(i)[1] for i in greetings]
print(p2)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
o = [x for x in digits if x % 2 != 0]
print(o)

k = []
for j in digits:
    if j % 2 != 0:
        k.append(j)
print(k)