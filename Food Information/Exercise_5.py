print("This Program take a food information from the User:")
def new_date():
    import datetime
    return datetime.datetime.now()

while 'true':
    name_values = input("Enter values for (Asad, usman and haroon)or(1, 2, 3): ")
    if (name_values == 'asad') or (name_values == 'usman') or (name_values == 'haroon') or (name_values == '1') or (name_values == '2') or (name_values == '3'):
        if (name_values == 'asad') or (name_values == '1'):
            while 'true':
                write_or_read = input("What do you want? do you wanna write data or read data. Enter (1=write, 2=read): ")
                if (write_or_read == 'write') or (write_or_read == '1'):
                    with open("asad.txt", 'a') as f:
                        food = input("Enter Food which asad eta : ")
                        if food == "nothing":
                            print("okay")
                        else:
                            f.write(food+" : " + str(new_date()) + "\n")
                    print("Do you want else")
                elif write_or_read == 'read' or (write_or_read == '2'):
                    with open("asad.txt", 'r') as f:
                        a = f.read()
                        print(a)
                    print("Do you want else")
                else:
                    print("Okay")
                    break

        if (name_values == 'usman') or (name_values == '2'):
            while 'true':
                write_or_read = input("What do you want? do you wanna write data or read data. Enter (1=write, 2=read): ")
                if (write_or_read == 'write') or (write_or_read == '1'):
                    with open("usman.txt", 'a') as f:
                        food = input("Enter Food which usman eaten or else(nothing) : ")
                        if food == "nothing":
                            print("okay")
                        else:
                            f.write(food+" : " + str(new_date()) + "\n")
                    print("Do you want else")
                elif write_or_read == 'read' or (write_or_read == '2'):
                    with open("usman.txt", 'r') as f:
                        a = f.read()
                        print(a)
                    print("Do you want else")
                else:
                    print("Okay")
                    break
        if (name_values == 'haroon') or (name_values == '3'):
            while 'true':
                write_or_read = input(
                    "What do you want? do you wanna write data or read data. Enter (1=write, 2=read): ")
                if (write_or_read == 'write') or (write_or_read == '1'):
                    with open("haroon.txt", 'a') as f:
                        food = input("Enter Food which haroon eta : ")
                        if food == "nothing":
                            print("okay")
                        else:
                            f.write(food + " : " + str(new_date()) + "\n")
                    print("Do you want else")
                elif write_or_read == 'read' or (write_or_read == '2'):
                    with open("haroon.txt", 'r') as f:
                        a = f.read()
                        print(a)
                    print("Do you want else")
                else:
                    print("Okay")
                    break
    else:
        print("Try again and read the program clearly. ")
        exit(0)
