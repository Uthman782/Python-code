import time

t = time.strftime('%H:%M:%S')
print("The Time is : ", t)
h = int(time.strftime('%H'))
# h = int(input("Enter Hours : "))
if 0 <= h <= 12:  # (h >= 0 and h <= 12:)
    print("Good Morning Sir !")
elif 12 < h <= 17:  # (h > 12 and h <= 17)
    print("Good Afternoon Sir !")
elif 17 < h <= 19:
    print("Good Evening Sir !")
elif 19 < h > 0:
    print("Good Night Sir !")
else:
    pass
