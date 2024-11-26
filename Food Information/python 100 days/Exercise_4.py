a = input("Enter Your Name:  ")
# print(a[1])
SumWord = ""
print("Take it Opposite ")
for word in a.split(" "):
    if len(word) > 2:
        word = word[2] + word[1] + word[3:] + word[0]
    elif len(word) == 1:
        word = word
    else:
        word = word[-1:] + word[0]
    print(word, end=" ")
    SumWord = SumWord + word + " "

print()
print("Take it Normal")
# print(SumWord)
for word in SumWord.split(" "):
    if len(word) > 2:
        word = word[-1:] + word[1:2] + word[0:1] + word[2:-1]
    elif len(word) == 1:
        word = word
    else:
        word = word[-1:] + word[0:1]
    print(word, end=" ")
