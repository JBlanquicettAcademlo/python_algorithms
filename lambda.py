# return cubic
lambda_func = lambda x: x**3 
"""
>>> lambda_func(3)
27
>>> lambda_func(4)
64
"""

lambda_func = lambda x: True if "a" in x else False
"""
>>> lambda_func("Manzana")
True
>>> lambda_func("Limon")
False
>>> lambda_func("Pera")
True
"""

class Employee:

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    
    def __str__(self) -> str:
        return f"{self.name} {self.salary}"

employee1=Employee('Jorge', 1)
employee2=Employee('Jose', 100)
employee3=Employee('Billy', 150)
employee4=Employee('Radha', 2)
employee5=Employee('Andres', 0)

employee_list = [employee1, employee2, employee3, employee4, employee5]
sorted_employee_salary = sorted(employee_list, key=lambda employee: employee.salary)

"""
>>> for e in sorted_employee_salary:
>>>     print(e)
Andres 0
Jorge 1
Radha 2
Jose 100
Billy 150
"""
