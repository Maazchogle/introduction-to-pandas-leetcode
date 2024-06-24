# 2879. Display the First Three Rows
# Easy
# Companies
# Hint
# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.

 

# Example 1:

# Input:
# DataFrame employees
# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  |
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+
# Output:
# +-------------+---------+-------------+--------+
# | employee_id | name    | department  | salary |
# +-------------+---------+-------------+--------+
# | 3           | Bob     | Operations  | 48675  |
# | 90          | Alice   | Sales       | 11096  |
# | 9           | Tatiana | Engineering | 33805  |
# +-------------+---------+-------------+--------+
# Explanation: 
# Only the first 3 rows are displayed

Solution :

import pandas as pd

# Sample data or actual data setup
data = {'employee_id': [3, 90, 9, 60, 49, 43],
        'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
        'department': ['Operations', 'Sales', 'Engineering', 'IT', 'HR', 'Admin'],
        'salary': [48675, 11096, 33805, 37678, 23793, 40454]}

# Create the DataFrame
employees = pd.DataFrame(data)

# Function to return the first 3 rows of the employees DataFrame
def selectFirstRows(df):
    return df.head(3)

# Example usage:
first_3_rows = selectFirstRows(employees)
print(first_3_rows)
