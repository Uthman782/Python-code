# factorial
# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
#
#
# number = int(input("Enter the Number for Factorial: "))
# x = factorial(number)
# print(x)

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# number2 = int(input("Enter the Number for factorial: "))
# print(factorial(number2))
def series(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return series( n - 1) + series(n - 2)


number3 = int(input("Enter the Value for this series :"))
print(series(number3))
# series(number3)
#