class Employee:
    def __init__(self, name, field, id, salary):
        self.name = name
        self.job = field
        self.id = id
        self.salary = salary

    def printDaitel(self):
        return f"Name of the Employee is {self.name}, Field of the Employee is {self.job} and Id No of the employee is {self.id}"

    def __repr__(self):
        return f"This is Employee class Object for {self.name}"

    def __add__(self, other):
        return int(self.salary) + int(other.salary)

emp1 = Employee("Usman", "Data Science", 72, '5000')
emp2 = Employee("Asad", "Web Developer", 98, '2700')
# print(emp1.printDaitel())
# print(emp1)
print(emp1 + emp2)
