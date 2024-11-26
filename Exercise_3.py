print("\tThere are 5 chances for you to give right Answer.")
i = 0
while i <= 5:
    a = int(input("Enter Your choice: "))
    if a > 100:
        print('The Right value is less than 100. Pleas enter value less then 100.')
    elif a == 25:
        print("\tYou Win this Game!.")
        print("\tThe Value is :", a)
        r = 1
        print("|", end="")
        while r < 50:
            print("#", end="")
            r = r + 1
        while r < 50:
            print("-", end="")
            r = r + 1
        print("|", end="")
        break
    elif a < 25:
        print('\tYour Enter value is less than!')
        r = 1
        print("|", end="")
        while r < a:
            print("#", end="")
            r = r + 1
        while r < 50:
            print('-', end="")
            if r == 25:
                print("|", end="")
            r = r + 1
        print("|")
    elif a > 25:
        if a > 25:
            print('\tYour Enter value is Greater than!')
        elif a > 50:
            print('\tYour Enter value is More Greater than!')
        r = 1
        print("|", end="")
        while r < a:
            print("#", end="")
            if r == 25:
                print("|", end="")
            r = r + 1
        while r < 50:
            print("-", end="")
            r = r + 1
        print("|")
    if i == 5:
        print("\t\t\tYou are loser!")
    i = i + 1
