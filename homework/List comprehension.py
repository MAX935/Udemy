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

#
#
# greetings = ['hello', 'hi', 'hey', 'hola']
# p = []
# for i in greetings:
#     p.append(list(i)[1])
# print(p)
#
# p2 = [list(i)[1] for i in greetings]
# print(p2)
#
#
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# o = [x for x in digits if x % 2 != 0]
# print(o)
#
# k = []
# for j in digits:
#     if j % 2 != 0:
#         k.append(j)
# print(k)
#
#
# dic1 = {'audi': 'a3', 'bmw': 3, 'key3': True}
# print(dic1)
#
# dict2 = {key:value  for key,value in dic1.items()}
# print(dict2)

# from random import randint
# k = [randint(-10,20) for k in range(10)]
# print(k)
#
# dict5 = {key: key ** 3 for key in k}
# print(dict5)
#
# dict6 = {d:'Positive' if d > 0 else 'Negative' if d < 0 else 'Null' for d in dict5.keys()}
# print(dict6)
#
# from random import randint
# k = [randint(-10,20) for k in range(10)]
# print(k)
#

ln = [[1,2,4],[1,5,6],[1,54,3]]
print(len(ln[0]))

