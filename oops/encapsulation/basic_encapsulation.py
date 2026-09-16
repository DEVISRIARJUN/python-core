class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary Cannot be negative")
        self.__salary = value
c = Employee("nanda",40000)
print(c.name)
c.salary = 70000
print(c.salary)
