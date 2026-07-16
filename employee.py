from sql_executor import execute


def add_employee():
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print(f"\nEntering details for employee {i + 1}:")
        emp_id = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        dept = input("Enter department: ")
        salary = int(input("Enter salary: "))

        query = f"INSERT INTO emp(id, name, age, dept,sal) VALUES ({emp_id}, '{name}', {age}, '{dept}',{salary})"
        execute(query)

    print(f"\n{n} employee(s) processed.")


def update_employee():
    update_id = int(input("Enter the employee ID you want to update: "))

    check_query = f"SELECT * FROM emp WHERE id = {update_id}"
    exists = execute(check_query)
    
    if exists:
        print("Employee found. Enter new details:")
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        dept = input("Enter new department: ")
        salary = int(input("Enter new salary: "))

        query = f"UPDATE emp SET name='{name}', age={age}, dept='{dept}',sal={salary} WHERE id={update_id}"
        execute(query)
        print("\nEmployee updated successfully!")
    else:
        print("\nError: Employee ID not found.")


def delete_employee():
    delete_id = int(input("Enter the employee ID you want to delete: "))

    query = f"DELETE FROM emp WHERE id = {delete_id}"
    rows_affected = execute(query)

    if rows_affected and rows_affected > 0:
        print("\nEmployee deleted successfully!")
    else:
        print("\nError: Employee ID not found.")


# In main.py
def view_employees():
    query = "SELECT * FROM emp"
    employees = execute(query)

    if not employees:
        print("\nNo employees to display.")
        return [] # Return an empty list instead of None
    else:
        print("\n--- Employee List ---")
        for emp in employees:
            print(emp)
        return employees