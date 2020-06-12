CREATE DEFINER=`root`@`localhost` PROCEDURE `update_book`(IN id int, IN newName varchar(45), IN newPublisher INT)
BEGIN
	IF newName != '' THEN
		UPDATE tbl_book b
        SET b.title = newName
        WHERE b.bookid = id;
	END IF;	
	
    IF newPublisher > 0 THEN
		UPDATE tbl_book b
        SET b.pubId = newPublisher
        WHERE b.bookid = id;
	END IF;	
    
END