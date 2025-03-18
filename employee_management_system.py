from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, emp_name, emp_dept):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_dept = emp_dept

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._emp_id}")
        print(f"Employee Name: {self._emp_name}")
        print(f"Department: {self._emp_dept}")

class PermanentEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, base_salary, extra_bonus):
        super().__init__(emp_id, emp_name, emp_dept)
        self._base_salary = base_salary
        self._extra_bonus = extra_bonus

    def calculate_salary(self):
        return self._base_salary + self._extra_bonus

    def display_details(self):
        super().display_details()
        print(f"Base Salary: ${self._base_salary:.2f}")
        print(f"Bonus: ${self._extra_bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, pay_rate, total_hours):
        super().__init__(emp_id, emp_name, emp_dept)
        self._pay_rate = pay_rate
        self._total_hours = total_hours

    def calculate_salary(self):
        return self._pay_rate * self._total_hours

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self._pay_rate:.2f}")
        print(f"Total Hours: {self._total_hours}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, monthly_stipend):
        super().__init__(emp_id, emp_name, emp_dept)
        self._monthly_stipend = monthly_stipend

    def calculate_salary(self):
        return self._monthly_stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._monthly_stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

# Example Usage
perm_emp = PermanentEmployee("2001", "Rahul", "Development", 75000, 7000)
contract_emp = ContractEmployee("2002", "Neha", "Marketing", 60, 170)
intern_emp = Intern("2045", "Amit", "Accounts", 2000)

perm_emp.display_details()
contract_emp.display_details()
intern_emp.display_details()
