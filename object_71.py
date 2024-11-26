class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def print_data(self):
        print(f"Employee Name is {self.name} and his work in this place is {self.job}.")

obj = Employee('Usman', 'Data Science')
obj.print_data()
# print(type(obj))
# print(type("what about you gone take to me."))
# print(id(obj))
print(dir(obj))
import inspect
print(inspect.getmembers(obj))
