import os

class Employee:
    def __init__(self, employee_id, name, designation, salary):
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.salary = salary

def add_employee(employee_id, name, designation, salary):
    employee = Employee(employee_id, name, designation, salary)

    with open("employee_data.txt", "a") as data_file:
        file_position = data_file.tell()
        data_file.write(f"{employee.employee_id},{employee.name},{employee.designation},{employee.salary}\n")

    index_file[employee_id] = file_position

def delete_employee(employee_id):
    if employee_id not in index_file:
        print("Employee not found.")
        return

    del index_file[employee_id]

    with open("employee_data.txt", "w") as data_file:
        for emp_id, file_position in index_file.items():
            data_file.seek(file_position)
            record = data_file.readline().strip()
            data_file.write(record + "\n")

def display_employee(employee_id):
    if employee_id not in index_file:
        print("Employee not found.")
        return

    with open("employee_data.txt", "r") as data_file:
        data_file.seek(index_file[employee_id])
        record = data_file.readline().strip()
        employee_data = record.split(",")
        print("Employee ID:", employee_data[0])
        print("Name:", employee_data[1])
        print("Designation:", employee_data[2])
        print("Salary:", employee_data[3])

# Check if the data file exists, if not create it
if not os.path.isfile("employee_data.txt"):
    with open("employee_data.txt", "w"):
        pass

# Load the index file into memory
index_file = {}
if os.path.isfile("index_file.txt"):
    with open("index_file.txt", "r") as index_file_handle:
        for line in index_file_handle:
            employee_id, file_position = line.strip().split(",")
            index_file[employee_id] = int(file_position)

# User interaction
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Display Employee Details")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        salary = input("Enter Salary: ")
        add_employee(employee_id, name, designation, salary)
        print("Employee added successfully.")

    elif choice == "2":
        employee_id = input("Enter Employee ID to delete: ")
        delete_employee(employee_id)
        print("Employee deleted successfully.")

    elif choice == "3":
        employee_id = input("Enter Employee ID to display details: ")
        display_employee(employee_id)

    elif choice == "4":
        # Save the index file before exiting
        with open("index_file.txt", "w") as index_file_handle:
            for employee_id, file_position in index_file.items():
                index_file_handle.write(f"{employee_id},{file_position}\n")
        break

    else:
        print("Invalid choice. Please try again.")

print("Exiting Employee Management System.")
