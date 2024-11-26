class Rectangle:
    def shap_rec(self):
       print("\t\t\t\t\t\t\t__________________________")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t|                        |")
       print("\t\t\t\t\t\t\t__________________________")

class Triangle:
    def shap_tri(self):
        print("\t\t\t\t\t\t\t          __")
        print("\t\t\t\t\t\t\t         /  \ ")
        print("\t\t\t\t\t\t\t        /    \ ")
        print("\t\t\t\t\t\t\t       /      \ ")
        print("\t\t\t\t\t\t\t      /        \ ")
        print("\t\t\t\t\t\t\t     /          \ ")
        print("\t\t\t\t\t\t\t    /____________\ ")

class Square:
    def shap_squ(self):
        print("\t\t\t\t\t\t\t____________________")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t|                  |")
        print("\t\t\t\t\t\t\t____________________")

class Shap(Rectangle, Triangle, Square):
    def __init__(self, name):
        self.shap_name = name

    def aboutShap(self):
        print(f"I am {self.shap_name}.")

rec = Shap("Rectangle")
squ = Shap("Square")
tri = Shap("Triangle")
rec.aboutShap()
rec.shap_rec()
tri.aboutShap()
tri.shap_tri()
squ.aboutShap()
squ.shap_squ()