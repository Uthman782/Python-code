def summation():
    """This is a function which take input from the user and sum this values."""
    a = int(input("Enter your first Number: "))
    b = int(input("Enter Second Number: "))
    sum1 = a + b
    return sum1


def mul():
    """This is a function which multiply tow number:"""
    a = int(input("Enter the Number a: "))
    b = int(input("Enter the number v: "))
    print("Result of Multiplication: ", a * b)


print(summation.__doc__)
v = summation()
print("Your Result is: ", v)
print(mul.__doc__)
mul()