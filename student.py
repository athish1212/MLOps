from sql_executor1 import execute


def add_student():
    n = int(input("Enter number of student: "))

    for i in range(n):
        print(f"\nEntering details for student {i + 1}:")
        emp_id = int(input("Enter usn: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        dept = input("Enter department: ")
        fee=int(input("Enter fee: "))

        query = f"INSERT INTO stud(id, name, age, dept,fee) VALUES ({emp_id}, '{name}', {age}, '{dept}',{fee})"
        execute(query)

    print(f"\n{n} student(s) processed.")


def update_student():
    update_id = int(input("Enter the student usn you want to update: "))

    check_query = f"SELECT * FROM stud WHERE id = {update_id}"
    exists = execute(check_query)

    if exists:
        print("Student found. Enter new details:")
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        dept = input("Enter new department: ")
        fee = int(input("Enter new fee: "))

        query = f"UPDATE stud SET name='{name}', age={age}, dept='{dept}',fee={fee} WHERE id={update_id}"
        execute(query)
        print("\nStudent updated successfully!")
    else:
        print("\nError: Student ID not found.")


def delete_student():
    delete_id = int(input("Enter the Student ID you want to delete: "))

    query = f"DELETE FROM stud WHERE id = {delete_id}"
    rows_affected = execute(query)

    if rows_affected and rows_affected > 0:
        print("\nStudent deleted successfully!")
    else:
        print("\nError: Student ID not found.")


# In main.py
def view_student():
    query = "SELECT * FROM stud"
    employees = execute(query)

    if not employees:
        print("\nNo Students to display.")
        return [] # Return an empty list instead of None
    else:
        print("\n--- Student List ---")
        for emp in employees:
            print(emp)
        return employees
