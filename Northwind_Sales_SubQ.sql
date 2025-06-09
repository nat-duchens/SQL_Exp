SELECT ProductID, SUM(Quantity) AS Total_Sales,
	(SELECT Price FROM Products WHERE OrderDetails.ProductID = ProductID) 
	AS Prices,
	(SUM(Quantity) * (SELECT Price FROM Products WHERE OrderDetails.ProductID = ProductID )) 
	AS Total_Raised,
	(SELECT ProductName FROM Products WHERE OrderDetails.ProductID = ProductID)
	AS P_Names
FROM OrderDetails
GROUP BY ProductID 
-- ORDER BY Total_Sales DESC
ORDER BY Total_Raised DESC

