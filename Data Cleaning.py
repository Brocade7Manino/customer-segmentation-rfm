import pandas as pd

#Read data
df = pd.read_csv("online_retail.csv", encoding='ISO-8859-1')

print(df.head())
print(df.info())
print(df.describe())

#Check for missing values
print(df.isnull().sum())

#Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

#Remove outliers
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

#Format data
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(str)

#Add TotalPrize
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

#Check
print(df.head())
print(df.info())

#Save
df.to_csv("OnlineRetail_cleaned.csv", index=False, encoding='utf-8')