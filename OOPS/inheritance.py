class Protiviti:

    def __init__(self, vertical):
        self.__vertical = vertical

    def project(self, project_name, duration):
        self.__project_name = project_name
        self.__duration = duration

    def get_project_details(self):
        return f"Project name is {self.__project_name} and duration is {self.__duration}"

    def get_vertical(self):
        return self.__vertical


class Details(Protiviti):

    def assign_project_to_employee(self, project_name, duration, emp_name):
        super().project(project_name, duration)
        self.emp_name = emp_name

    def __str__(self):
        return f"Employee: {self.emp_name}, {self.get_project_details()}, Vertical: {self.get_vertical()}"


# Usage
p = Details("pss")
p.assign_project_to_employee("successware", 4, "nitin chaudhary")

print(p)  # This will use the __str__ method of Details
