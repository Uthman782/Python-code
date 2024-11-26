def sum(num1, num2):
    print('Hello SUM Function')
    return num1 + num2
def sub(num1, num2):
    def another_function(num3, num4):
        return num3 - num4
    # print(another_function)
    return another_function

if __name__ == '__main__':
    sum = sum(2, sum(6, sum(5, sum(7, sum(8, sum(9, 0))))))
    print(sum)
    # sub = sub(10, 5)
    # print("Your Subtraction is: ", sub)
    sub1 = sub(0, 0)
    print(sub1(20, 5))


