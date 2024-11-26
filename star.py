n = int(input("Enter the Number for Loop Rows: "))
while 'true':
    name = input("What do you want to print: ")
    c = 1
    if name == "exit()":
        exit(0)
    else:
        while n >= c:
            a = n
            b = 0
            while a >= c:
                print(" ", end=" ")
                a = a - 1
            while b < c:
                print(name, end="  ")
                b = b + 1
            d = 1
            while d < b:
                print(name, end="  ")
                d = d + 1
            print("")
            c = c + 1
        c = 2
        while c <= n:
            a = 0
            b = n
            while a < c:
                print(" ", end="  ")
                a = a + 1
            while b > c:
                print(name, end="  ")
                b = b - 1
            d = n
            while d >= b:
                print(name, end="  ")
                d = d - 1
            print("")
            c = c + 1
