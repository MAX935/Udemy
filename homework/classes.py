# # class Devices:
# #     count = 10
# #
# #     def __init__(self, name, ram, color, sale):
# #         self.name = name
# #         self.ram = ram
# #         self.color = color
# #         self.sale = sale
# #
# # iphone = Devices('iphone 12 pro', 256, 'blue', True)
# #
# #
# # print(iphone.color)
# # print(Devices.count)
#
#
# class BlogPost:
#     def __init__(self, username, text, number_of_likes):
#         self.username = username
#         self.text = text
#         self.number_of_likes = number_of_likes
#
#
# sobolev = BlogPost('Sobolev', 'Wall', 1050)
# avtorevizorro = BlogPost('Avtorevizorro', 'Cars', 2000)
#
# sobolev.number_of_likes = 1900
#
# print(sobolev.number_of_likes)
# print(avtorevizorro.number_of_likes)
#


class BankAccount:
    balance = 0

    def __init__(self, client_id, client_first_name, client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

    def Add(self, value):
        BankAccount.balance += value

    def withdraw(self, value):
        BankAccount.balance -= value


