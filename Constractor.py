class Student:
    no_std = 150

    def __init__(self):
        print("O! Hello how are you to run this Object.")
        s_name = input("Enter Your Name: ")
        s_marks = input("Enter your Marks: ")
        s_roll = input("Enter Your Roll No: ")
        self.name = s_name
        self.marks = s_marks
        self.roll = s_roll
        # print(f"Name of the Student is {s_name}, Roll No is {self.roll} And his marks is {self.marks}")

    def get_data(self):
        print(f"Name of the Student is {self.name}, Roll No is {self.roll} And his marks is {self.marks}")

    @classmethod
    def change_value(cls):
        cls.no_std = 155
        print("Changing have completed")
# i = 0
# while i < 5:
obj = Student()
# obj.get_data()
    # i += 1
print(obj.no_std)
obj1 = Student()
obj.change_value()
print(obj1.no_std)
