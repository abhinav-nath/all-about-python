import pandas as pd

# create a dictionary
data = {'Name': ['John', 'Tom', 'Henry', 'Stacy', 'Sarah'],
        'Age': [38, 45, 34, 27, 29]}

df = pd.DataFrame(data)

print(df['Name'])
print(df['Age'])
