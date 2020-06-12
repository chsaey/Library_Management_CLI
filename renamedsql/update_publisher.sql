CREATE DEFINER=`root`@`localhost` PROCEDURE `update_publisher`(IN id int, IN newName varchar(45), IN newAddr varchar(45), In newPhone varchar(45))
BEGIN
	IF newName != '' THEN
		UPDATE tbl_publisher p
        SET p.publisherName = newName
        WHERE p.publisherid = id;
	END IF;
	IF newAddr != '' THEN
		UPDATE tbl_publisher p
        SET p.publisherAddress = newAddr
        WHERE p.publisherid = id;
	END IF;
    IF newPhone != '' THEN
		UPDATE tbl_publisher p
        SET p.publisherPhone = newPhone
        WHERE p.publisherid = id;
	END IF;
END