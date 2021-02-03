# """
# У вас есть класс Time с состоянием time, который обозначает секунды.
# У вас должно быть 2 метода. Один переводит в минуты, второй в часы.
# Пример-230 секунд переводит 3:50 и 0:3:50
# """
# import datetime
# class Time:
#     def __init__(self):
#         self.time = int(input('Enter a number: '))
#         self.ask =input("Хочешь веревести в часы? (y/n): ")
#
#
#     def convert_to_minutes(self):
#         if self.ask == 'n':
#             print(f'{self.time // 60}:{self.time % 60}')
#
#     def convert_to_hour(self):
#         if self.ask == "y":
#             a = str(datetime.timedelta(seconds=self.time))
#             print(a)
#
# time = Time()
# time.convert_to_minutes()
# time.convert_to_hour()


# """
# Write a class called Password_manager. The class should have a list called old_passwords
# that holds all of the user’s past passwords. The last item of the list is the user’s current password. There should be a method called get_password that returns the current password
# and a method called set_password that sets the user’s password. The set_password
# method should only change the password if the attempted password is different from all
# the user’s past passwords. Finally, create a method called is_correct that receives a string
# and returns a boolean True or False depending on whether the string is equal to the current
# password or not.
# """
#
#
# class PasswordManager:
#     old_passwords = ['asdfasd', '1232134123', 'asdfg']
#
#     def set_password(self, password):
#         self.old_passwords.append(password)
#
#     def get_password(self):
#         return self.old_passwords[-1]
#
#     def is_correct(self):
#         if self.old_passwords == True:
#             print(True)
#         else:
#             print(False)
#
#
# manager = PasswordManager()
# manager.set_password(password=input('Enter a password: '))
# print(manager.get_password())
# # manager.is_correct()
# """
# Write a program that draws “modular rectangles” like the ones below.
# The user specifies the
# width and height of the rectangle, and the entries start at 0 and increase
# typewriter fashion
# from left to right and top to bottom, but are all done mod 10.
# Below are examples of a 3 × 5
# rectangle and a 4 × 8. NOTE: Use just ONE LOOP!!!
# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4
# 0 1 2 3 4 5 6 7
# 8 9 0 1 2 3 4 5
# 6 7 8 9 0 1 2 3
# 4 5 6 7 8 9 0 1
# """
# # class Matrix:
# #     def __init__(self):
# #         self.a, self.b = map(int, input('Enter a numbers: ').split())
# #     def get_matrix(self, ):
# #         counter = 0
# #         while counter != int(self.a) and int(self.b):
# #             print(counter % 10, end=' ')
# #             counter += 1
#         print()
# matrix = Matrix()
# matrix.get_matrix()
