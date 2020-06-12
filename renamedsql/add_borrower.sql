CREATE DEFINER=`root`@`localhost` PROCEDURE `add_borrower`(IN name char(50), IN address char(50), IN phone char(12))
BEGIN
IF NOT exists (Select * From tbl_borrower b where b.name = name and b.address = address and b.phone = phone)
Then
	INSERT INTO tbl_borrower(name, address, phone)
	VALUES(name, address, phone);
END IF;
END