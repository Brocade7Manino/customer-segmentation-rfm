--Top Customers
SELECT CustomerID,
       SUM(TotalPrice) AS total_spent
FROM OnlineRetail_cleaned orc 
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;

--Mothly Revenue
SELECT strftime('%Y-%m', InvoiceDate) AS month,
       SUM(TotalPrice) AS revenue
FROM OnlineRetail_cleaned orc
GROUP BY month
ORDER BY month;

--Top Products
SELECT Description,
       SUM(Quantity) AS total_sold
FROM OnlineRetail_cleaned orc
GROUP BY Description
ORDER BY total_sold DESC
LIMIT 10;