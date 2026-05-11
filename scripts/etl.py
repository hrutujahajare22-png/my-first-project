import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("output/employees.csv", index=False)

print("ETL Process Completed")