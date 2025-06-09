SELECT ProductID,
	Quantity,
		(SELECT Price FROM Products WHERE OrderDetails.ProductID = ProductID) 
	As Prices,
	(SELECT ProductName FROM Products WHERE OrderDetails.ProductID = ProductID) 
	As P_Names
FROM OrderDetails
ORDER BY ProductID