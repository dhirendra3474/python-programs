import pandas as pd
employee_data = {
    'Employee_ID': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
    'Name': ['Aarav Sharma', 'Priya Patel', 'Amit Verma', 'Sneha Reddy', 'Vikram Singh', 'Neha Gupta'],
    'Age': [28, 34, 41, 25, 38, 29],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT', 'Sales'],
    'Role': ['Software Engineer', 'HR Manager', 'Financial Analyst', 'SEO Specialist', 'DevOps Engineer', 'Sales Executive'],
    'Joining_Date': ['2022-03-15', '2021-06-01', '2023-01-10', '2024-02-20', '2020-11-05', '2023-08-12'],
    'Salary': [75000, 65000, 85000, 55000, 95000, 62000],
    'Performance_Score': [4.5, 4.2, 3.8, 4.7, 4.1, 3.9],
    'Status': ['Active', 'Active', 'Active', 'Active', 'On Leave', 'Active']
}

df=pd.DataFrame(employee_data)
print(df)
print(df.info())
print(df.describe())

# Sorting in single columns
print(df.sort_values("Age"))

# Sorting in descending order
print(df.sort_values("Salary",ascending=False))

# Sort by multiple columns
df1=df.sort_values(["Performance_Score","Salary"],ascending=[True,False])
print(df1)

# Aggregation Methods
print(df["Age"].sum())
print(df['Age'].max())
print(df['Age'].min())
print(df['Age'].count())
print(df['Salary'].sum())
print(df['Salary'].min())
print(df['Salary'].max())
print(df['Salary'].count())



