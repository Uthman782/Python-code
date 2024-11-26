def decoration(func1):
    def func_for_return():
        print("Before Execution....")
        func1();
        print("After Execution....")
    return func_for_return

@decoration
def func1():
    print(f"Hi Usman Khan")

# func1()

print(10//2)