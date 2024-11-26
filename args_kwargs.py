def func_Args(normal, *args, **kwargs):
    for item in args:
        print(item, end=" ")
    print(normal)

list = []
key = 0
number = input('Enter How many values: ')
while key < int(number):
    print("Enter the Value: ")
    a = input()
    list.insert(key, a)
    key = key + 1

func_Args(88, *list)
