
class EmployeeClass:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department
    
    def display_details(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}"
