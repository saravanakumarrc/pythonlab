class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("name={} age={}".format(self.name, self.age))

class Employee(Person):
    def __init__(self, name, age, designation):
        super(Employee, self).__init__(name,age)
        self.designation = designation

    def print(self):
        super(Employee, self).print();
        print("designation={}".format(self.designation))

saravana = Employee("saravana", 31, "Software engineer")
saravana.print()
print(saravana.__repr__())
print(saravana.__str__())
print(saravana.__dict__())

