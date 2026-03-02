import pandas as pd

# 1. Loading the Employee Dataset
file_path = 'employees.xlsx'
try:
    df = pd.read_excel(file_path)
    pd.set_option('display.max_columns', None, 'display.width', 1000)
    print("--- Employee Dataset Analysis ---\n")
except Exception as e:
    print(f"Error loading {file_path}: {e}")
    exit()

# 2. Basic Stats (1-8)
print(f"1) Total entries: {len(df)}")
print(f"2) Number of departments: {df['DEPARTMENT_ID'].nunique()}")
print(f"3) Max salary per department:\n{df.groupby('DEPARTMENT_ID')['SALARY'].max()}")
print(f"4) Employee(s) with minimum salary:\n{df[df['SALARY'] == df['SALARY'].min()]}")
print(f"5) Total salary per department:\n{df.groupby('DEPARTMENT_ID')['SALARY'].sum()}")
print(f"6) Number of managers: {df['MANAGER_ID'].nunique()}")
print(f"7) Employees per department:\n{df['DEPARTMENT_ID'].value_counts().sort_index()}")
print(f"8) Maximum salary in organization: {df['SALARY'].max()}")

# 3. Job and Manager Details (9-14)
print(f"9) Employees with Job_id = SA_MAN:\n{df[df['JOB_ID'] == 'SA_MAN']}")
print(f"10) Average salary per department:\n{df.groupby('DEPARTMENT_ID')['SALARY'].mean()}")
print(f"11) Total employees per manager:\n{df['MANAGER_ID'].value_counts()}")

# 4. Commission Calculation (12)
df['COMMISSION_PCT'] = pd.to_numeric(df['COMMISSION_PCT'], errors='coerce').fillna(0)
df['COMMISSION_AMOUNT'] = df['SALARY'] * df['COMMISSION_PCT']
max_comm = df.loc[df['COMMISSION_AMOUNT'].idxmax()]
print(f"12) Max Commission: {max_comm['FIRST_NAME']} {max_comm['LAST_NAME']} (Amt: {max_comm['COMMISSION_AMOUNT']})")

# 5. Designation Analysis (13-14)
print(f"13) Job wise maximum salary:\n{df.groupby('JOB_ID')['SALARY'].max()}")
print(f"14) Job wise total salary:\n{df.groupby('JOB_ID')['SALARY'].sum()}")
