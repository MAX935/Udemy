# # # def calc():
# # # # #     """
# # # # #     Print Hello
# # # # #     :return: None
# # # # #     """
# # # # #     print('Hello!')
# # # # # calc()
# # # # # help(calc)
# # # # #
# # # # #
# # # # #
# # # # # def sum(a = 0, c = 10):
# # # # #     """
# # # # #
# # # # #     :param a:
# # # # #     :param c:
# # # # #     :return:
# # # # #     """
# # # # #     return a + c
# # # # #
# # # # # x = sum(23,42345)
# # # # # print(x)
# # # # #
# # # # #
# # # # # def is_hello(text):
# # # # #     if 'hello' in text:
# # # # #         return True
# # # # #     else:
# # # # #         return False
# # # # #
# # # # # z=is_hello('sklfsdgjohgoiejhello')
# # # # # print(z)
# # # # #
# # # # def car (company, model):
# # # #     return company in model
# # # #
# # # # print(car('audiaudiaudi','audi'))
# # #
# # #
# # # # zadanie 1
# # # def cat_voice():
# # #     print('Meow!')
# # #
# # #
# # # cat_voice()
# # #
# # #
# # # def dog_voice():
# # #     print('Woof!')
# # #
# # #
# # # dog_voice()
# # #
# # #
# # # # zadanie 2
# # #
# # # def cat_voice():
# # #     return 'Meow!'
# # #
# # #
# # # cat_voice()
# # #
# # #
# # # def dog_voice():
# # #     return 'Woof!'
# # #
# # #
# # # a = cat_voice()
# # # print(a * 2)
# # #
# # # b = dog_voice()
# # # print(b * 2)
# # #
# # #
# # # # 3 zadanie
# # # def get_voice(text):
# # #     return text + '!'
# # #
# # #
# # # # 4 zadanie
# # #
# # # def range_list(a, b):
# # #     return [k for k in range(a, b + 1) if k % 2 != 0]
# # #
# # #
# # # def list_of_range(k, m):
# # #     l=[]
# # #     for x in range(k, m+1):
# # #         if x % 2 != 0:
# # #             l.append(x)
# # #     return l
# # #
# # # # ARGS KWARGS
# # #
# # #

def func(*args):
    print(args)

func(10,20)