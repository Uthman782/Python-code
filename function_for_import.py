def add(n1, n2):
    return n1 + n2
def fact(n1):
    if n1 == 1:
        return 1
    elif n1 == 0:
        return 0
    else:
        return n1 * fact(n1 - 1)

print("This is :", __name__, "file")
if __name__ == '__main__':
    print("this is factorial of 5: ", fact(5))
