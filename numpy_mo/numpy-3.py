import numpy as np
# l1 = [2, 5, 7, 8, 9, 20]
# print(l1[0:3])
npl1 = np.array([3, 5, 8, 9, 0, 22])
print(npl1.ndim)
print(npl1[0:4])
# npl2 = np.array([[3, 4, 5], [8, 9, 7]])
# print(npl2[0:, 0:2])
# for i in npl2.flat:
#     print(i)
# a = np.arange(6).reshape(3, 2)
# b = np.arange(6).reshape(2, 3)
# print(a)
# print(b)
a = np.arange(30).reshape(3, 10)
# print(a)
# print(np.hsplit(a, 3))
# print(a)
# print(a.sum(axis=1))
b = a > 15
# print(b)
# print(a[b])
a[b] = 0
print(a)