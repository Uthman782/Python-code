# f = open('text.txt', 'r')
# text = f.read()
# print(text)
# f.close()
# fwrite = open('text.txt', 'w')
# fwrite.write("text is just here.")
# fwrite.close()
# fR = open('text.txt', 'r')
# reading = fR.read()
# print(reading)
# fR.close()
#
# with open('text.txt', 'a') as f:
#     f.write("Hello World !")

# f = open('text.txt', 'r')
# t = f.read()
# print(t)
i = 0
f = open('text.txt', 'r')
while True:
    line = f.readline()
    i += 1
    if not line:
        break
    m0 = line.split(",")[0]
    m1 = line.split(",")[1]
    m2 = line.split(",")[2]
    Sname = ''
    if i == 1:
        Sname = 'Usman Khan'
    elif i == 2:
        Sname = 'Jawad Khan'
    else:
        Sname = 'Suliman shah'
    print(f"The Maths Marks of {Sname}: {m0}")
    print(f"The C.Sci Marks of {Sname}: {m1}")
    print(f"The Physc Marks of {Sname}: {m2}")
