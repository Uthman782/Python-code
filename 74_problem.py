n = int(input('How many values are enter: '))
ls = []
for i in range(1, n+1):
    value = input('Enter Values: ')
    ls.append(value)

set1 = [i for i in ls]
print(set1)
