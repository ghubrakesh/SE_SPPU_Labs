class EmployeeDatabase:
    def __init__(self):
        self.employees = {}
        self.next_employee_id = 1

    def add_employee(self, name, designation, salary):
        employee_id = self.next_employee_id
        self.next_employee_id += 1

        employee_info = {
            'name': name,
            'designation': designation,
            'salary': salary
        }

        self.employees[employee_id] = employee_info

        return employee_id

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Employee with ID {employee_id} has been deleted.")
        else:
            print(f"Employee with ID {employee_id} does not exist.")

    def display_employee_info(self, employee_id):
        if employee_id in self.employees:
            employee_info = self.employees[employee_id]
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee_info['name']}")
            print(f"Designation: {employee_info['designation']}")
            print(f"Salary: {employee_info['salary']}")
        else:
            print(f"Employee with ID {employee_id} does not exist.")


# Example usage
database = EmployeeDatabase()

# Add employees
emp1_id = database.add_employee("John Doe", "Manager", 5000)
emp2_id = database.add_employee("Jane Smith", "Developer", 4000)

# Display employee information
database.display_employee_info(emp1_id)
database.display_employee_info(emp2_id)

# Delete an employee
database.delete_employee(emp1_id)

# Display employee information after deletion
database.display_employee_info(emp1_id)
