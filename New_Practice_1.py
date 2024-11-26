# a, b, c = 1, 2, 3
# print(a, b, c)
# a, b, c, *other, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)    # 1
# print(b)    # 2
# print(c)    # 3
# print(other)      # [4, 5, 6, 7, 8]
# print(d)    # 9
# print(e)    # 10
#       Dictionary  here........
user = {
    'Name': 'Uthman',
    'Age': '20',
    'Class': '12th',
    'fname': 'Abdul Samad'
}
# print(user['fname'])
print(user.get('fname', 'Abdus Samad'))
print('Class' in user.keys())
print('Class' in user.values())
print(user.items())
user.clear()
print(user)
