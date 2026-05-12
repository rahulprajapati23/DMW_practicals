# Practical 3: Employee Data Exploration

import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "employees.xlsx")

def main():
    df = pd.read_excel(DATA_PATH)

    # 1 Total entries
    tot_entries = len(df)
    print(f"Total Entries in the employee dataset : {tot_entries}")

    # 2 Total departments
    tot_dep = df['DEPARTMENT_ID'].nunique()
    print(f"Total Departments in ABC organization? : {tot_dep}")

    # 3 Max salary per dept
    max_salary_dep = df.groupby('DEPARTMENT_ID')['SALARY'].max()
    print(f"Maximum Salary by Department:\n{max_salary_dep}\n")

    # 4 Employee with min salary
    min_salary = df.loc[df['SALARY'].idxmin()]
    print(f"Employee with Minimum Salary:\n{min_salary}\n")

    # 5 Total salary per dept
    tot_salary = df.groupby('DEPARTMENT_ID')['SALARY'].sum()
    print(f"Total Salary by Department:\n{tot_salary}\n")

    # 6 Total managers approx (JOB_ID contains 'MAN')
    tot_managers = df['JOB_ID'].str.contains('MAN').sum()
    print('Total Managers in the organization :', tot_managers)

    # 7 Employees per department
    emp_per_dep = df['DEPARTMENT_ID'].value_counts()
    print(f"Employees per Department:\n{emp_per_dep}\n")

    # 8 Max salary overall
    max_salary = df['SALARY'].max()
    print(f"Maximum Salary in the organization : {max_salary}\n")

    # 9 Employees with Job ID 'SA_MAN'
    emp_sa_man = df[df['JOB_ID'] == 'SA_MAN']
    print(f"Employees with Job ID 'SA_MAN':\n{emp_sa_man}\n")

    # 10 Average salary by dept
    avg_salary = df.groupby('DEPARTMENT_ID')['SALARY'].mean()
    print(f"Average Salary by Department:\n{avg_salary}\n")

    # 11 Employees per manager
    emp_per_manager = df['MANAGER_ID'].value_counts()
    print(f"Employees per Manager:\n{emp_per_manager}\n")

    # 12 Employee with max commission
    if 'COMMISSION_PCT' in df.columns and not df['COMMISSION_PCT'].isna().all():
        max_comm = df.loc[df['COMMISSION_PCT'].idxmax()][['FIRST_NAME','LAST_NAME','COMMISSION_PCT']]
        print(f"Employee with Maximum Commission:\n{max_comm}\n")

    # 13 Max salary by job
    max_salary_job = df.groupby('JOB_ID')['SALARY'].max()
    print(f"Maximum Salary by Job ID:\n{max_salary_job}\n")

    # 14 Total salary by job
    tot_salary_job = df.groupby('JOB_ID')['SALARY'].sum()
    print(f"Total Salary by Job ID:\n{tot_salary_job}\n")

if __name__ == '__main__':
    main()
