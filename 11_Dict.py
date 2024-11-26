# Dictionary is nothing but just key value pairs
# d1 = {}         # this is Dictionary
# l1 = []         # this is Sample List
# t1 = ()         # this is sample tuple
# print(type(d1))
# print(type(l1))
# print(type(t1))
# this is list
#      Key   :  value
d2 = {"Usman": "Mango", "Asad": "Apply", "Haroon": "Banana", "Azma": {"Morning": "Chay", "Afternoon": "Cheekan", "Night": "suok" }}
print("This is sample list: ", d2)
d2["Khan G"] = "Ages"
print("This is second list: ", d2)
print("Azma in the morning: ", d2["Azma"]["Morning"])
del d2["Khan G"]
print(d2)
d2.update({"Ror Bacha": "Bangan"})
print(d2)
print(d2.keys())
print(d2.items())
print(d2.values())

