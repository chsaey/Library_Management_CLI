CREATE DEFINER=`root`@`localhost` PROCEDURE `update_borrower`(IN cardNo int, IN name CHAR(50), IN address CHAR(50), IN phone CHAR(12))
BEGIN
	IF name != 'null' THEN
		UPDATE tbl_borrower b
        SET b.name = name
        WHERE b.cardNo = b.cardNo;
	END IF;
	IF address != 'null' THEN
		UPDATE tbl_borrower b
        SET b.address = address
        WHERE b.cardNo = b.cardNo;
	END IF;
	IF phone != 'null' THEN
		UPDATE tbl_borrower b
        SET b.phone = phone
        WHERE b.cardNo = b.cardNo;
	END IF;
END