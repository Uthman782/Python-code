from functools import lru_cache
import time
@lru_cache(maxsize=2)
def looping_number(n):
    print("Numbers from 1 to 100000")
    ls = [i for i in range(1, 100001)]
    for i in ls:
        print(i, " ", end="")
        if i % 100 == 0:
            print()
    else:
        print("Loops is successfully Completed!")
if __name__ == '__main__':
    looping_number(3)
    print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)
    looping_number(3)


    print("Hello")
