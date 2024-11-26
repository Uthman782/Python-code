class A:
    _var = "I am class A variable but i am protected"
    var = "I am class A variable"

    def __init__(self):
        self.var = "I am inside in constractor of Class A"
        self.var1 = "Yes I am also inside in class A"
        self.spacial = "I am Spaicla var of constractor of class A"

class B(A):
    var = "I am class B variable"

    def __init__(self):
        self.var = "I am inside in constractor of Class B"
        self.var1 = "Yes I am also inside in class B"
        super().__init__()
        self.spacial = "I am Spaicla var of constractor of class B"


obj = A()
print(obj._var)
print(obj.var)
# print(obj.var1)
# print(obj.spacial)
obj2 = B()
print(obj2.var)
print(obj2.var1)
print(obj2.spacial)


