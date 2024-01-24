class Employee:
    num_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_employees += 1

    def average_salary(self, *salaries):
        total_salary = sum(salaries) + self.salary
        num_employees = len(salaries) + 1  
        return total_salary / num_employees


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_worked):
        super().__init__(name, family, salary, department)
        self.hours_worked = hours_worked

    def calculate_monthly_salary(self):
        return self.salary * (self.hours_worked / 40)  


employee1 = Employee("Vardhan", "Narra", 45000, "HR")
employee2 = FullTimeEmployee("Harsha", "Pattepur", 60000, "Engineering", 45)

average_salary_result = employee1.average_salary(55000, 60000, 70000)
monthly_salary_result = employee2.calculate_monthly_salary()

print(f"Number of employees: {Employee.num_employees}")
print(f"Average salary: {average_salary_result}")
print(f"Monthly salary for full-time employee: {monthly_salary_result}")
