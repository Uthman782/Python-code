from abc import ABC, abstractmethod
# class shap(ABC):
#     @abstractmethod
#     def printAria(self):
#         return 0
# class Rectangle(shap):
#     def __init__(self):
#         self.width = 10
#         self.height = 20
#
#     def printAria(self):
#         return self.width * self.height
#
# rec = Rectangle()
# print(rec.printAria())

class Shap(ABC):
    def __init__(self, name):
        self.shap_name = name

    @abstractmethod
    def aboutShap(self):
        return 0

class Rectangle(Shap):
    def shap_rec(self):
       print("\t\t\t\t\t\t\t__________________________")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t__________________________")

    def aboutShap(self):
        print(f"I am {self.shap_name}.")

class Triangle(Shap):
    def shap_tri(self):
        print("\t\t\t\t\t\t\t          __")
        print("\t\t\t\t\t\t\t         /  \ ")
        print("\t\t\t\t\t\t\t        /    \ ")
        print("\t\t\t\t\t\t\t       /      \ ")
        print("\t\t\t\t\t\t\t      /        \ ")
        print("\t\t\t\t\t\t\t     /          \ ")
        print("\t\t\t\t\t\t\t    /____________\ ")

    def aboutShap(self):
        print(f"I am {self.shap_name}.")

class Square(Shap):
    def shap_squ(self):
        print("\t\t\t\t\t\t\t____________________")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t____________________")

    def aboutShap(self):
        print(f"I am {self.shap_name}.")

rec = Rectangle("Rectangle")
squ = Square("Square")
tri = Triangle("Triangle")
rec.aboutShap()
rec.shap_rec()
tri.aboutShap()
tri.shap_tri()
squ.aboutShap()
squ.shap_squ()