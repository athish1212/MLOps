import employee
import student as std
import cross_analysis  # Import your new engine module

while True:
    print("\n==========================================")
    print("       MAIN MANAGEMENT SYSTEM MENU       ")
    print("==========================================")
    print("1. Employee Records Management")
    print("2. Student Records Management")
    print("3. Export & Generate Cross-Analysis Data")
    print("4. Exit Program")

    try:
        choice = int(input("\nEnter choice (1-4): "))
    except ValueError:
        print("Please enter a number.")
        continue

    match choice:
        case 1:
            while True:
                print("\n--- Employee Management System (MySQL) ---")
                print("1. Add Employee")
                print("2. Update Employee")
                print("3. Delete Employee")
                print("4. View Employees")
                print("5. Back to Main Menu")
                try:
                    sub_choice = int(input("\nEnter choice (1-5): "))
                except ValueError:
                    continue
                match sub_choice:
                    case 1:
                        employee.add_employee()
                    case 2:
                        employee.update_employee()
                    case 3:
                        employee.delete_employee()
                    case 4:
                        employee.view_employees()
                    case 5:
                        break
        case 2:
            while True:
                print("\n--- Student Management System (MySQL) ---")
                print("1. Add Student")
                print("2. Update Student")
                print("3. Delete Student")
                print("4. View Students")
                print("5. Back to Main Menu")
                try:
                    sub_choice = int(input("\nEnter choice (1-5): "))
                except ValueError:
                    continue
                match sub_choice:
                    case 1:
                        std.add_student()
                    case 2:
                        std.update_student()
                    case 3:
                        std.delete_student()
                    case 4:
                        std.view_student()
                    case 5:
                        break
        case 3:
            cross_analysis.export_combined_data()
        case 4:
            print("Exiting program... Goodbye!")
            break
