import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sql_executor import execute as execute_emp
from sql_executor1 import execute as execute_stud


def plot_net_position(net_data):
    """Generates the visual breakdown of net profit/loss by business units."""
    if not net_data:
        print("[Warning] No data available to plot.")
        return

    # Color map matches your exact specification
    color_map = {'CSE': 'red', 'ECE': 'blue', 'ISE': 'yellow'}

    departments = list(net_data.keys())
    values = [net_data[d] for d in departments]
    colors = [color_map.get(d, 'gray') for d in departments]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(departments, values, color=colors, edgecolor='black')

    # Add numeric labels on top/bottom of each bar
    for bar, val in zip(bars, values):
        height = bar.get_height()
        va = 'bottom' if height >= 0 else 'top'
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'${int(val):,}', ha='center', va=va, fontweight='bold')

    ax.axhline(0, color='black', linewidth=1.5)
    ax.set_xlabel("Department")
    ax.set_ylabel("Net Financial Position ($)")
    ax.set_title("Net Profit / Loss Summary by Department (Live Data)")

    # Build legend dynamically
    baseline_patch = mpatches.Patch(color='lightgray', label='Y=0 Baseline (Break-even)')
    legend_patches = [baseline_patch]
    for dept in departments:
        legend_patches.append(mpatches.Patch(color=color_map.get(dept, 'gray'),
                                             label=f'{dept} ({color_map.get(dept, "gray").capitalize()})'))
    ax.legend(handles=legend_patches, loc='upper left')

    plt.tight_layout()
    print(" -> Displaying financial visual analysis window...")
    plt.show()


def export_combined_data():
    print("\nFetching Employee data (ID, Department, Salary)...")
    emp_query = "SELECT id, department, sal FROM emp"
    employees = execute_emp(emp_query)

    print("Fetching Student data (ID, Department, Fee)...")
    stud_query = "SELECT id, dept, fee FROM stud"
    students = execute_stud(stud_query)

    if not employees and not students:
        print("[Error] No records discovered in either database to export.")
        return

    emp_list = employees if employees else []
    stud_list = students if students else []

    # 1. Export Employee Financial Datasets
    if emp_list:
        try:
            with open('employee_financials.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'department', 'sal'])
                writer.writeheader()
                writer.writerows(emp_list)
            print(" -> Successfully generated 'employee_financials.csv'")
        except Exception as e:
            print(f"[Error] Failed to write employee CSV: {e}")

    # 2. Export Student Financial Datasets
    if stud_list:
        try:
            with open('student_financials.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'department', 'fee'])
                for row in stud_list:
                    writer.writerow([row.get('id'), row.get('dept'), row.get('fee')])
            print(" -> Successfully generated 'student_financials.csv'")
        except Exception as e:
            print(f"[Error] Failed to write student CSV: {e}")

    # 3. Aggregate Institutional Summary by Business Units
    dept_summary = {}
    for emp in emp_list:
        d = emp['department'].strip().upper() if emp.get('department') else 'UNKNOWN'
        dept_summary[d] = dept_summary.get(d, {'salary_expenses': 0, 'fee_revenues': 0})
        dept_summary[d]['salary_expenses'] += float(emp.get('sal') or 0)

    for stud in stud_list:
        d = stud['dept'].strip().upper() if stud.get('dept') else 'UNKNOWN'
        dept_summary[d] = dept_summary.get(d, {'salary_expenses': 0, 'fee_revenues': 0})
        dept_summary[d]['fee_revenues'] += float(stud.get('fee') or 0)

    # Dictionary to hold the real data for our chart mapping: { DEPT: NET_POSITION }
    live_net_data = {}

    try:
        with open('department_summary.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['department', 'total_salary_expense', 'total_fee_revenue', 'net_financial_position'])
            for dept, metrics in dept_summary.items():
                net = metrics['fee_revenues'] - metrics['salary_expenses']
                writer.writerow([dept, metrics['salary_expenses'], metrics['fee_revenues'], net])

                # Capture the real numbers right here for the chart
                live_net_data[dept] = net

        print(" -> Successfully generated unified analysis file: 'department_summary.csv'")
        print("[Success] CSV Data written.")

        # Trigger the live plot execution!
        plot_net_position(live_net_data)

    except Exception as e:
        print(f"[Error] Failed to write summary CSV or plot data: {e}")


if __name__ == '__main__':
    export_combined_data()