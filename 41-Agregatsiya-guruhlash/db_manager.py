import psycopg2
from psycopg2.extras import DictCursor
import datetime

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "lesson3",
    "password": "lesson3",
    "database": "lesson3"
}

def execute_db_operation(query, params=None, fetch_results=True):
    connection = None
    cursor = None
    data = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=DictCursor)
        cursor.execute(query, params)
        if fetch_results:
            data = cursor.fetchall()
        else:
            connection.commit()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return data

def initialize_database():
    try:
        execute_db_operation("CREATE TYPE VALID_SALARY_STATUS AS ENUM ('paid', 'pending', 'delayed')", fetch_results=False)
        print("Status type created.")
    except psycopg2.errors.DuplicateObject:
        print("Status type already exists.")

    table_creation_query = """
    CREATE TABLE IF NOT EXISTS salaries (
        id SERIAL PRIMARY KEY,
        employee_name VARCHAR NOT NULL,
        month VARCHAR(7) NOT NULL CHECK (month ~ '^\d{4}-\d{2}$'),
        base_salary NUMERIC NOT NULL CHECK (base_salary >= 0),
        bonus NUMERIC DEFAULT 0 CHECK (bonus >= 0),
        penalty NUMERIC DEFAULT 0 CHECK (penalty >= 0),
        net_salary NUMERIC GENERATED ALWAYS AS (base_salary + bonus - penalty) STORED,
        status VALID_SALARY_STATUS DEFAULT 'pending'
    );
    """
    execute_db_operation(table_creation_query, fetch_results=False)
    print("Salaries table is ready.")

def add_new_salary_entry():
    employee = input("Enter employee's full name: ").strip()
    if not employee:
        print("Employee name cannot be empty.")
        return

    while True:
        payment_month = input("Enter month (YYYY-MM, e.g., 2024-07): ").strip()
        try:
            datetime.datetime.strptime(payment_month, '%Y-%m')
            if len(payment_month) != 7: raise ValueError
            break
        except ValueError:
            print("Invalid month format. Use YYYY-MM.")

    base = float(input("Enter base salary: "))
    extra_bonus = float(input("Enter bonus (0 if none): "))
    deduction = float(input("Enter penalty (0 if none): "))

    add_query = """
    INSERT INTO salaries (employee_name, month, base_salary, bonus, penalty, status)
    VALUES (%s, %s, %s, %s, %s, 'pending');
    """
    execute_db_operation(add_query, (employee, payment_month, base, extra_bonus, deduction), fetch_results=False)
    print(f"Salary entry added for '{employee}' for '{payment_month}'.")

def show_employee_salaries():
    employee_to_find = input("Employee name (leave blank for all): ").strip()
    month_to_filter = input("Month (YYYY-MM, leave blank for all): ").strip()

    search_query = "SELECT * FROM salaries WHERE 1=1"
    query_params = []

    if employee_to_find:
        search_query += " AND employee_name ILIKE %s"
        query_params.append(f"%{employee_to_find}%")
    if month_to_filter:
        search_query += " AND month = %s"
        query_params.append(month_to_filter)

    search_query += " ORDER BY employee_name, month DESC"
    results = execute_db_operation(search_query, tuple(query_params))

    if not results:
        print("No records found.")
        return

    print("\n--- Employee Salaries ---")
    for record in results:
        print(f"ID: {record['id']}, Employee: {record['employee_name']}, Month: {record['month']}, "
              f"Base: {record['base_salary']:.2f}, Bonus: {record['bonus']:.2f}, "
              f"Penalty: {record['penalty']:.2f}, Net: {record['net_salary']:.2f}, "
              f"Status: {record['status']}")

def show_monthly_salary_list():
    while True:
        target_month = input("Enter month (YYYY-MM) for salary list: ").strip()
        try:
            datetime.datetime.strptime(target_month, '%Y-%m')
            if len(target_month) != 7: raise ValueError
            break
        except ValueError:
            print("Invalid month format. Use YYYY-MM.")

    monthly_query = "SELECT * FROM salaries WHERE month = %s ORDER BY employee_name"
    results = execute_db_operation(monthly_query, (target_month,))

    if not results:
        print(f"No salaries found for '{target_month}'.")
        return

    print(f"\n--- {target_month} Salary List ---")
    for record in results:
        print(f"ID: {record['id']}, Employee: {record['employee_name']}, "
              f"Base: {record['base_salary']:.2f}, Bonus: {record['bonus']:.2f}, "
              f"Penalty: {record['penalty']:.2f}, Net: {record['net_salary']:.2f}, "
              f"Status: {record['status']}")

def show_outstanding_salaries():
    outstanding_query = "SELECT * FROM salaries WHERE status IN ('pending', 'delayed') ORDER BY status, employee_name, month"
    results = execute_db_operation(outstanding_query)

    if not results:
        print("No unpaid or delayed salaries.")
        return

    print("\n--- Unpaid / Delayed Salaries ---")
    for record in results:
        print(f"ID: {record['id']}, Employee: {record['employee_name']}, Month: {record['month']}, "
              f"Net: {record['net_salary']:.2f}, Status: {record['status']}")

def change_salary_status():
    record_id_input = input("Enter record ID to change status: ").strip()
    if not record_id_input.isdigit():
        print("ID must be a number.")
        return

    while True:
        new_status = input("Enter new status ('paid', 'pending', 'delayed'): ").strip().lower()
        if new_status in ['paid', 'pending', 'delayed']:
            break
        else:
            print("Invalid status. Choose 'paid', 'pending', or 'delayed'.")

    update_query = "UPDATE salaries SET status = %s WHERE id = %s RETURNING *"
    updated_record = execute_db_operation(update_query, (new_status, int(record_id_input)), fetch_results=True)

    if updated_record:
        print(f"Status for record ID {record_id_input} changed to '{new_status}'.")
    else:
        print(f"Record ID {record_id_input} not found.")

def get_total_paid_for_month():
    while True:
        month_for_total = input("Enter month (YYYY-MM) for total paid salary: ").strip()
        try:
            datetime.datetime.strptime(month_for_total, '%Y-%m')
            if len(month_for_total) != 7: raise ValueError
            break
        except ValueError:
            print("Invalid month format. Use YYYY-MM.")

    total_query = "SELECT SUM(net_salary) AS total_paid FROM salaries WHERE month = %s AND status = 'paid'"
    result = execute_db_operation(total_query, (month_for_total,))

    if result and result[0]['total_paid'] is not None:
        print(f"\nTotal paid for '{month_for_total}': {result[0]['total_paid']:.2f}")
    else:
        print(f"No paid salaries found for '{month_for_total}'.")

def find_employee_with_most_bonus():
    most_bonus_query = "SELECT employee_name, SUM(bonus) AS total_bonus FROM salaries GROUP BY employee_name ORDER BY total_bonus DESC LIMIT 1"
    result = execute_db_operation(most_bonus_query)

    if result:
        print(f"\nEmployee with most bonus: {result[0]['employee_name']} (Total: {result[0]['total_bonus']:.2f})")
    else:
        print("No bonus data.")

def find_employee_with_most_penalty():
    most_penalty_query = "SELECT employee_name, SUM(penalty) AS total_penalty FROM salaries GROUP BY employee_name ORDER BY total_penalty DESC LIMIT 1"
    result = execute_db_operation(most_penalty_query)

    if result:
        print(f"\nEmployee with most penalty: {result[0]['employee_name']} (Total: {result[0]['total_penalty']:.2f})")
    else:
        print("No penalty data.")

def main_app_menu():
    initialize_database()

    while True:
        print("\n--- Salary Monitor Menu ---")
        print("1. Add new salary")
        print("2. View employee salaries")
        print("3. View monthly salary list")
        print("4. View outstanding salaries")
        print("5. Change salary status")
        print("--- Reports ---")
        print("6. Total paid for a month")
        print("7. Employee with most bonus")
        print("8. Employee with most penalty")
        print("0. Exit")

        user_choice = input("Enter your choice: ").strip()

        if user_choice == '1': add_new_salary_entry()
        elif user_choice == '2': show_employee_salaries()
        elif user_choice == '3': show_monthly_salary_list()
        elif user_choice == '4': show_outstanding_salaries()
        elif user_choice == '5': change_salary_status()
        elif user_choice == '6': get_total_paid_for_month()
        elif user_choice == '7': find_employee_with_most_bonus()
        elif user_choice == '8': find_employee_with_most_penalty()
        elif user_choice == '0':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")

if __name__ == "__main__":
    main_app_menu()