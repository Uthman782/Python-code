try:
    f1 = open('usman.txt')
except Exception as e:
    print(e)
    print("This is Exception...!")
else:
    print("this is not Exception this is else part.")

finally:
    print("This is just finally..")

