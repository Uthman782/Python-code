import random
rand1 = random.random() * 100
rand2 = random.randint(0, 10)
# print(rand1)
# print(int(rand1))
# print(rand2)
# list1 = ['Haroon', 'asad', 'Usman', 'azma', 'aayma']
# choices = random.choice(list1)
# print(choices)
bool_first = "come and he declare that he wanna bool first"
bat_first = "come and he declare that he wanna bat first"
print("This is mach. and the time is come for the tase.\n"
      " there are two teams one is pakistan and another is india\n"
      " please enter which team is came for the tase first:  ")
inp_for_tase = input("Enter Pakistan or India only: ")
i = inp_for_tase
if (i == 'pakistan') or (i == 'india') or (i == 'Pakistan') or (i == 'India') or (i == 'PAKISTAN') or (i == 'INDIA'):
    random_tase = random.randint(0, 1)
    if random_tase == 1:
        print("Oh! India loss this tase and ", end=" ")
        print("Pakistan win the Tase:")
        bool_or_bat = input("What is your choices (Babar Azam) to select (enter bat or bool): ")
        if bool_or_bat == 'bat':
            print(f"So Babar Azam {bat_first}: ")
            print("And india have bool first ")
        elif bool_or_bat == 'bol' or bool_or_bat == 'bool':
            print(f"So Babar Azam {bool_first}: ")
            print("And india have bat first ")
        else:
            print("Sorry What do you means that!")

    else:
        print("Oh! Pakistan loss this tase and ", end=" ")
        print("India win the Tase:")
        bool_or_bat = input("What is your choices (Virate Kooly) to select (enter bat or bool): ")
        if bool_or_bat == 'bat':
            print(f"So Virate Kooly {bat_first}: ")
            print("And pakistan have bool first ")
        elif bool_or_bat == 'bol' or bool_or_bat == 'bat':
            print(f'So Virate Kooly {bool_first}: ')
            print("And pakistan have bat first ")
        else:
            print("Sorry What do you means that!")
else:
    print("You are wrong the MACH is between PAKISTAN and INDIA:")
