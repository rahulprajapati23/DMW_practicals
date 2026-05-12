# Practical 3: Employee Data Exploration - Simple Version

import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(SCRIPT_DIR, "employees.xlsx"))

print("1. Total entries:", len(df))
print("2. Total departments:", df['DEPARTMENT_ID'].nunique())
print("3. Max salary by department:\n", df.groupby('DEPARTMENT_ID')['SALARY'].max())
print("4. Employee with minimum salary:\n", df.loc[df['SALARY'].idxmin()])
print("5. Total salary by department:\n", df.groupby('DEPARTMENT_ID')['SALARY'].sum())
print("6. Total managers:", df['JOB_ID'].str.contains('MAN').sum())
print("7. Employees per department:\n", df['DEPARTMENT_ID'].value_counts())
print("8. Max salary in organization:", df['SALARY'].max())
print("9. Employees with Job ID 'SA_MAN':\n", df[df['JOB_ID'] == 'SA_MAN'])
print("10. Average salary by department:\n", df.groupby('DEPARTMENT_ID')['SALARY'].mean())
print("11. Employees per manager:\n", df['MANAGER_ID'].value_counts())
print("12. Employee with max commission:\n", df.loc[df['COMMISSION_PCT'].idxmax()][['FIRST_NAME', 'LAST_NAME', 'COMMISSION_PCT']])
print("13. Max salary by job:\n", df.groupby('JOB_ID')['SALARY'].max())
print("14. Total salary by job:\n", df.groupby('JOB_ID')['SALARY'].sum())
