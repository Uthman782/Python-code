# ls = []
# for i in range(50):
#     if i % 3 == 0:
#         ls.append(i)
#
# print(ls)
# List Comprehensions
# ls = [i for i in range(1, 51) if i % 5 == 0]
ls = [i*2 for i in range(1, 51)]
# print(ls)

# Dict Comprehensions
# dict1 = {i: f"item{j}" for j in range(10000) if j % 100 == 0 for i in range(100)}
dict1 = {j: f"item{j}" for j in range(10000) if j % 100 == 0}
dict1 = {value: key for key, value in dict1.items()}
# print(dict1)
# set Comprehensions
set1 = {'usman', 'asad', 'khan', 'uthman', 'haroon', 'khan', 'uthman'}
set2 = {i for i in set1}
# print(set2)
# generate Comprehensions
evens = (i for i in range(10) if i % 2 == 2)
print(type(evens))
def gen(n):
    for i in range(n):
        yield i

g = gen(10)
print(g.__next__())
