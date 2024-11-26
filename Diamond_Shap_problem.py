class A:
    def met(self):
        print("I am Method of class A")


class B(A):
    def met(self):
        print("I am Method of class B")

class C(A):
    def met(self):
        print("I am Method of class C")

class D(B, C):
    def met(self):
        print("I am Method of class D")


a = A()
b = B()
c = C()
d = D()
d.met()
