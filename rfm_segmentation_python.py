import pandas as pd

#Read data
df = pd.read_csv(r"C:\Users\云叶\Desktop\ecommerce_analysis\OnlineRetail_cleaned.csv")
print(df.head())

#Counting date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
max_date = df["InvoiceDate"].max()

#Recency
recency = df.groupby("CustomerID")["InvoiceDate"].max()
recency = (max_date - recency).dt.days

#Frequency
frequency = df.groupby("CustomerID")["InvoiceNo"].nunique()

#Monetary
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
monetary = df.groupby("CustomerID")["TotalPrice"].sum()

rfm = pd.DataFrame({
    "Recency": recency,
    "Frequency": frequency,
    "Monetary": monetary
})

#Rate
rfm["R_score"] = pd.qcut(rfm["Recency"].rank(method="first"), 5, labels=[5,4,3,2,1])
rfm["F_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_score"] = pd.qcut(rfm["Monetary"].rank(method="first"), 5, labels=[1,2,3,4,5])

#Segment
def segment(row):
    if row["R_score"] >= 4 and row["F_score"] >= 4 and row["M_score"] >= 4:
        return "VIP"
    elif row["R_score"] >= 3 and row["F_score"] >= 3:
        return "Loyal"
    elif row["R_score"] <= 2:
        return "At Risk"
    else:
        return "Regular"

rfm["Segment"] = rfm.apply(segment, axis=1)
rfm["Segment"].value_counts()

#Visualization

import matplotlib.pyplot as plt

rfm["Segment"].value_counts().plot(kind="bar")
plt.title("Customer Segments Distribution")
plt.show()

rfm.to_csv(r"C:\Users\云叶\Desktop\ecommerce_analysis\RMF.csv", index=True)