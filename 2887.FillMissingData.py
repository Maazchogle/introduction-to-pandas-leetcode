2887. Fill Missing Data
Easy
Companies
Hint
DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.

 

Example 1:
Input:+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Explanation: 
The quantity for Wristwatch and WirelessEarbuds are filled by 0.


solution :


import pandas as pd

def fillMissingValues(df):
    # Fill missing values in 'quantity' column with 0
    df['quantity'] = df['quantity'].fillna(0)
    # Convert quantity column to integer type
    df['quantity'] = df['quantity'].astype(int)
    return df

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
        'quantity': [None, None, 779, 849],
        'price': [135, 821, 9319, 3051]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Apply the function
    result_df = fillMissingValues(df)
    
    # Display the result
    print(result_df)
