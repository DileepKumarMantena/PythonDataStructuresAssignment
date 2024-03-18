from employee import EmployeeClass
from department import Department

if __name__ == "__main__":
    engineering_department = Department("Engineering")

    # Create Employees
    employee1 = EmployeeClass("John Doe", 1001, "Software Engineer", "Engineering")
    employee2 = EmployeeClass("Jane Smith", 1002, "Project Manager", "Engineering")
    employee3 = EmployeeClass("Alice Johnson", 1003, "QA Engineer", "Engineering")

    # Add Employees to the Department
    engineering_department.add_employee(employee1)
    engineering_department.add_employee(employee2)
    engineering_department.add_employee(employee3)

    # List Employees in the Department
    engineering_department.list_employees()

    # Remove an Employee from the Department
    engineering_department.remove_employee(employee2)

    # List Employees again to see the changes
    engineering_department.list_employees()
