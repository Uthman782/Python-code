class Student:
    avg = 71.9

    def __init__(self, name, maths, cs, eng):
        self.name = name
        self.maths = maths
        self.cs = cs
        self.eng = eng

    def printData(self):
        print(f"Your Name: {self.name}\n"
              f"Your Maths:{self.maths}\n"
              f"Your Computer Science: {self.cs}\n"
              f"Your English: {self.eng}")
class Player:
    avg = 76.4

    def __init__(self, name, score, maths, cs, eng):
        Student.__init__(self, name, maths, cs, eng)
        self.name = name
        self.pscore = score

    def score(self):
        print(f"Name: {self.name} and his Score: {self.pscore}")

class P_student(Player, Student):
    avg = 81.4

usman = P_student("Usman", 10, 84, 89, 72)
usman.printData()
usman.score()
print(usman.avg)
