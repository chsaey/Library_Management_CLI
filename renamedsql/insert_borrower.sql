CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_borrower`(IN BName varchar(45), IN BAddress varchar(45), IN BPhone varchar(12), out result int)
BEGIN
IF not Exists(SELECT * FROM tbl_borrower b WHERE b.name = BName and b.address = BAddress and b.phone = BPhone) 
THEN
INSERT INTO tbl_borrower (name, address, phone)
VALUES(BName, BAddress, BPhone); 
set result = 1;
else
set result = 0;
END IF;
END