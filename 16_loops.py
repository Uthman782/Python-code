list1 = ["88", "66", 6, 7, 5, 4, 3, 8, 9, 10, 200, 20, 11]
# for items in list1:
#     if items >= 6:
#         print(items)
# for items in list1:
#     if str(items).isnumeric() and int(items) >= 6:
#         print("Number: ", items)

# list3 = []
# i = 0
# while i < 5:
#     print("Enter the Number at index ", i, end=": ")
#     a = input()
#     list3.insert(i, a)
#     i = i+1
# b = input("Enter number to Remove: ")
# list3.remove(b)
# list3.sort()
# print("Your Enter Number is: ", end=" ")
# for item in list3:
#     print(item, end=" ")
i = 0
while True:
    a = input("Enter the Value But less than 100: ")
    if int(a) > 100:
        print("You Enter ", a)
        break
    elif int(a) < 100:
        print("Hello!")
        continue
    print("Hay!")


