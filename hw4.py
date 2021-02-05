"""Cортировка подсчетом"""
# a = list(map(int, input('Enter number:').split()))
# num = [0] * 11
# for i in a:
#     num[i] += 1
# for j in range(len(num)):
#     for u in range(num[j]):
#         print(j, end= '')

"""Подсчет пузырком"""
# a = 7
# b = [5, 4, 2, 8, 9, 1, 6]
# g = 0
# for i in range(a-1):
#     for j in range(a-1):
#         if b[j]>b[j+1]:
#             g += 1
#             b[j],b[j+1] = b[j+1], b[j]
#     print(b)
# print(g)