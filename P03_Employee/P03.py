import pandas as pd

def analyze_employees():
    file_path = 'employees.xlsx'
    
    try:
        # Load the dataset
        df = pd.read_excel(file_path)
        
        # Display settings to ensure output looks good
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)

        print("--- Employee Dataset Analysis ---\n")

        # 1) How many entries are there in the employee dataset?
        print("1) Total entries in the dataset:", len(df))
        print("-" * 40)

        # 2) How many departments are there in ABC organization?
        num_departments = df['DEPARTMENT_ID'].nunique()
        print("2) Number of departments:", num_departments)
        print("-" * 40)

        # 3) Find out the maximum salary that is given in each department?
        print("3) Maximum salary in each department:")
        print(df.groupby('DEPARTMENT_ID')['SALARY'].max())
        print("-" * 40)

        # 4) Find out the detail of the employee who have got the minimum salary in the entire organization?
        min_salary_employee = df[df['SALARY'] == df['SALARY'].min()]
        print("4) Employee(s) with minimum salary:")
        print(min_salary_employee)
        print("-" * 40)

        # 5) Find out the total salary amount that is given in each department?
        print("5) Total salary per department:")
        print(df.groupby('DEPARTMENT_ID')['SALARY'].sum())
        print("-" * 40)

        # 6) Find out how many managers work in the organization?
        num_managers = df['MANAGER_ID'].nunique()
        print("6) Number of managers working in the organization:", num_managers)
        print("-" * 40)

        # 7) Find out that how many employee works in each department?
        print("7) Number of employees in each department:")
        print(df['DEPARTMENT_ID'].value_counts().sort_index())
        print("-" * 40)

        # 8) Find out what is the maximum salary that is given to employee in this organization?
        print("8) Maximum salary in the organization:", df['SALARY'].max())
        print("-" * 40)

        # 9) Find the details of all the employees whose Job_id = SA_MAN.
        print("9) Details of employees with Job_id = SA_MAN:")
        print(df[df['JOB_ID'] == 'SA_MAN'])
        print("-" * 40)

        # 10) Find the average salary of each department?
        print("10) Average salary of each department:")
        print(df.groupby('DEPARTMENT_ID')['SALARY'].mean())
        print("-" * 40)

        # 11) Find the number of employees working under every manager in the organization.
        print("11) Number of employees working under every manager:")
        print(df['MANAGER_ID'].value_counts())
        print("-" * 40)

        # 12) Extract the name of the employee taken maximum commission.
        df['COMMISSION_PCT'] = pd.to_numeric(df['COMMISSION_PCT'], errors='coerce').fillna(0)
        df['COMMISSION_AMOUNT'] = df['SALARY'] * df['COMMISSION_PCT']
        
        max_comm_idx = df['COMMISSION_AMOUNT'].idxmax()
        max_comm_employee = df.loc[max_comm_idx]
        
        print("12) Employee with maximum commission:")
        # Displaying name and absolute commission amount for clarity
        print(f"Name: {max_comm_employee['FIRST_NAME']} {max_comm_employee['LAST_NAME']}")
        print(f"Commission Amount: {max_comm_employee['COMMISSION_AMOUNT']}")
        print(f"(Based on Salary {max_comm_employee['SALARY']} * Commission Pct {max_comm_employee['COMMISSION_PCT']})")
        print("-" * 40)

        # 13) Extract designation wise salary maximum salary to the employees.
        print("13) Designation (Job_ID) wise maximum salary:")
        print(df.groupby('JOB_ID')['SALARY'].max())
        print("-" * 40)

        # 14) Extract designation wise salary total salary amount to the employees.
        print("14) Designation (Job_ID) wise total salary:")
        print(df.groupby('JOB_ID')['SALARY'].sum())
        print("-" * 40)

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_employees()
