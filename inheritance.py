class Student:
    def __init__(self, name, maths, cs, eng):
        self.name = name
        self.maths = maths
        self.cs = cs
        self.eng = eng

class StudentJob(Student):
    def get_data(self):
        self.total = int(self.cs) + int(self.eng) + int(self.maths)
        return f"Your Name is {self.name} your Marks are: \n Maths: {self.maths}\n Computer Science: {self.cs}\n English: {self.eng}\n Total Marks are ({self.total}) in 300."

    def avergae(self):
        total = self.total
        avg = (int(total) / 300) * 100
        print(f"Your avergae Marks are: {avg}")

obj1 = StudentJob("Usman", "84", "89", '68')
obj2 = Student("Usman", "74", "79", '58')
a = obj1.get_data()
# b = obj2.get_data()
print(a)
# print(b)
obj1.avergae()
