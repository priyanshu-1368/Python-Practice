class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def details(self):
        print(f"Employee Name      : {self.name}")
        print(f"Employee id        : {self.employee_id}")
        print(f"Employee Salary    : {self.basic_salary}")
        print("-" * 30)

class Manager(Employee):
    def __init__(self, name, employee_id, basic_salary, department):
        super().__init__(name, employee_id, basic_salary)
        self.department = department

    def show_manager(self):
        self.details()
        print("Department:",self.department)

class SeniorManager(Manager):
    def __init__(self, name, employee_id, basic_salary, department, bonus):
        super().__init__(name, employee_id, basic_salary, department)
        self.bonus = bonus

    def calculate_total_sal(self):
        total_sal = self.basic_salary + self.bonus
        self.show_manager()
        print("Total Salary:",total_sal)

emp1 = SeniorManager("Priyanshu", 1313 ,25000, "IT", 5000)
emp1.calculate_total_sal()