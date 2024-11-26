class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f"{f_name}.{l_name}@gmail.com"

    @property
    def email(self):
        if (self.f_name == None) or (self.l_name == None):
            return f"Sorry Email is not set.."
        else:
            return f"{self.f_name}.{self.l_name}@gmail.com"

    @email.setter
    def email(self, string):
        name = string.split("@")[0]
        self.f_name = name.split(".")[0]
        self.l_name = name.split(".")[1]

    @email.deleter
    def email(self):
        self.f_name = None
        self.l_name = None


emp1 = Employee("Usman", "Khan")
print(emp1.email)
emp1.f_name = "Asad"
print(emp1.email)
emp1.email = "this.that@email.com"
print(emp1.email)
print(emp1.f_name)
print(emp1.l_name)

del emp1.email
print(emp1.email)
