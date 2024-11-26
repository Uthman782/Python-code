x = 89
# print("I am Before this function:", x)
def func1():
    x = 20
    # print("I am in this Function: ", x)
    def inner_func():
        global x
        x = 88
    # print("This Before calling Function: ", x)
    inner_func()
    print("This after calling Function: ", x)
func1()
print("I am After this Function :", x)