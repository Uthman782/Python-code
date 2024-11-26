a = [[5, 7], [2, 3], [5, 4]]

print(a)
def sortting(a):
    return a[1]


y = sortting(a)
a.sort(key=sortting)
print(a)
