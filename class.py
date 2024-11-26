class MyClass:
    def __init__(self, name, sub, marks):
        self.name = name
        self.sub = sub
        self.marks = marks
        # print(f"Your Name is {self.name} And your Subject is {self.sub} And your Marks is {self.marks}.")

    def get_data(self):
        return f"Your Name is {self.name} And your Subject is {self.sub} And Your Marks are {self.marks}."

    @classmethod
    def from_dash(cls, string):
        # params = string.split('-')
        # return cls(params[0], params[1], params[2])
        return cls(*string.split('-'))

    @staticmethod
    def sample(name):
        print("Hello how are you? your class is finished."+name)
obj1 = MyClass("Usman", "C.Science", "420")
obj2 = MyClass("Asad", "Arts", "478")
obj3 = MyClass.from_dash("Haroon-Medical-504")
print(obj1.get_data())
print(obj2.get_data())
print(obj3.get_data())
obj3.sample('usman')
