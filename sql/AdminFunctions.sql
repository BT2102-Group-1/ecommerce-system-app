-- Admin Functions
SELECT table1.iid AS 'ProductID', table1.sold AS 'Number of "SOLD" items', table2.unsold AS 'Number of "UNSOLD" items'
FROM (SELECT productId AS iid, COUNT(productId) AS sold FROM Item WHERE purchaseStatus='Sold' GROUP BY productId) AS table1
INNER JOIN (SELECT productId AS iid, COUNT(productId) AS unsold FROM Item WHERE purchaseStatus='Unsold' GROUP BY productId) AS table2
ON table1.iid = table2.iid;