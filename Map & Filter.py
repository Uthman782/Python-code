# list1 = [2, 3, 4, 5, 6, 7, 8]
# list2 = list(map(str, list1))
# print(list1[1]+5)
# print(list1)
# list1 = list(map(lambda x: x * x, list1))
# print(list1)
#
# def square(a):
#     return a*a
# def cub(a):
#     return a * a * a
# func_list = [square, cub]
# for i in range(5):
#     list_sq = list(map(lambda x: x(i), func_list))
#     print("This is list square: ", list_sq)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def greater(x):
    return x > 5


new_list = list(filter(lambda x: x > 5, list1))
# new_list = list(filter(greater, list1))
print(new_list)

from functools import reduce
sum_list1 = reduce(lambda x, y: x + y, list1)
sum_new = reduce(lambda x, y: x + y, new_list)
print("Summation of new_list is: " + str(sum_new))
print("Summation of list1 is: " + str(sum_list1))
