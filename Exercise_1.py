Dict = {
    "Mutable": "Can Change",
    "Immutable": "Cannot Change",
    "English": "A Language",
    "Come": "Anaa"
}
a = input("Enter the Value to Search: ")
if a in Dict:
    print("Meaning of this Word is: ")
    print(Dict[a])
else:
    print("Sorry this word isn't our Dictionary.")


# dict1 = {}
# word = input("Enter the Word: ")
# value = input("Enter the meaning of this word: ")
# dict1[word] = value
# print(dict1)