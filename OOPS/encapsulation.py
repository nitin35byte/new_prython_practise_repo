class Employee():

    def __init__(self , name , age , salary):
        self.__name=name
        self.__age=age
        self.__salary=salary


    def get_age(self):
        return self.__age


    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def update_name(self ,new_name):

        if isinstance(new_name , str):
            self.__name=new_name
        return new_name

    def update_age(self , new_age):

        if new_age >0 and new_age <150 and isinstance(new_age, int):
            self.__age=new_age
        return new_age


    def update_salary(self , new_salary):
        if isinstance(new_salary , int):
            self.__salary=new_salary
        return new_salary

    def __str__(self):
        return f"Employee(Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary})"

e = Employee("John", 30, 50000)
print(e)  # Output: Employee(Name: John, Age: 30, Salary: 50000)

e.update_name("Rahul")
e.update_age(35)
e.update_salary(60000)
print(e)  # Out
e.update_name('rahul')
print(e)