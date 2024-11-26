import time
# print("Enter the number (less than 100): ")
# a = int(input())
# c = 0
# print("|", end=" ")
# while c < a:
#     print("#", end="")
#     time.sleep(0.066)
#     if c == 3 or c == 8 or c == 15 or c == 30 or c ==45 or c == 65:
#         time.sleep(0.155432212)
#     else:
#         time.sleep(0.07)
#     c += 1
# # print("hello")
# i = 0
# while i < (95-a):
#     print(".", end="")
#     if i == 35:
#         time.sleep(0.5)
#         print("USMAN", end="")
#     i += 1
# print(" |")
# print("\n Done yet")
print("this is ", __name__)
if __name__ == '__main__':
    a = time.asctime(time.localtime(time.time()))
    print(a)
