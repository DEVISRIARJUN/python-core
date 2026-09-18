# 4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        self.__log = []
    def get_salary(self):
        self.__log.append("Each Access is attempted")
        print("Salary : ",self.__salary)
    def update_salary(self,new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("updated Salary : ",self.__salary)
        else:
            print("Invalid salary")
    def log(self):
        print(self.__log)
e = Employee("arjun",25000)
e.get_salary()
e.update_salary(45000)
e.log()


    