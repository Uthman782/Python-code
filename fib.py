def fib(n):
    a, b, Sum = 0, 1, 0
    while a < n:
        Sum += a
        print(a, end=" ")
        a, b = b, a + b

    print("\nComplete Code. So after that Sum of all Values is : ", Sum)
print("Enter the value of n: ")
a = input()
fib(int(a))