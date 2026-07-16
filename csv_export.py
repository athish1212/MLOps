import main
import csv


def csv_convert():
    employees = main.view_employees()

    # Check if employees list is empty or None
    if not employees:
        print("No employees found to export.")
        return  # Stop execution early

    try:
        with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Map columns directly to the dictionary keys returned by your SQL query
            fieldnames = ['id', 'name', 'age', 'dept']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header row (ID, Name, Age, Department)
            writer.writeheader()

            # Write all employee rows automatically
            writer.writerows(employees)

        print("Data successfully exported to employees.csv")

    except Exception as e:
        print(f"An error occurred while exporting: {e}")


# Remember to actually call the function if running this file directly!
if __name__ == "__main__":
    csv_convert()