a = input("Enter 'quit' : ")
if a != 'quit':
    raise ValueError("You wanna enter only quit okay. ")

# a = int(input("Enter Value Between 5 and 9: "))
# if 5 > a or a > 9:
#     raise ValueError("The Value should be between 5 and 9.")

# try:
#     I = [6, 5, 4, 3, 2]
#     i = int(input("Enter Index: "))
#     print(I[i])
# except Exception as e:
#     print(e)
#     print("Some Error is Present ")
# finally:
#     print("This line of Code is Always executed always okay.")

# a = input("Enter a Number: ")
# print(f"Multiplication of {a} is: ")
# try:
#     a = int(a)
#     for i in range(11):
#         print(f"{i} X {a} = {i*a}")
# except Exception as e:
#     print(e)
#     print("Every thing is fine.")
