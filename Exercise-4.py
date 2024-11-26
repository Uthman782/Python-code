import time
n = int(input("Enter the Number for Loop Rows: "))
# i = 1
# while i <= n:
#     a = 0
#     while a < i:
#         print("x", end=" ")
#         a = a + 1
#     print("")
#     i = i + 1
# # print("")
# i = 0
# while i <= n:
#     i = i + 1
#     a = n
#     while a >= i:
#         print("x", end=" ")
#         a = a - 1
#     print("")
oldTime = time.time()
while 'true':
    name = input("What do you want to print: ")
    c = 1
    if name == "exit()":
        exit(0)
    else:
        while c <= n:
            a = n
            b = 0
            while a >= c:
                print(" ", end=" ")
                a = a - 1
            while b < c:
                print(name, end=" ")
                b = b + 1
            d = 1
            while d < b:
                print(name, end=" ")
                d = d + 1
            print("")
            c = c + 1
        c = 2
        while c <= n:
            a = 0
            b = n
            while a < c:
                print(" ", end=" ")
                a = a + 1
            while b > c:
                print(name, end=" ")
                b = b - 1
            d = n
            while d >= b:
                print(name, end=" ")
                d = d - 1
            print("")
            c = c + 1
        # break
        newTime = time.time() - oldTime
        print(newTime)
