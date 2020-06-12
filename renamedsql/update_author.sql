CREATE DEFINER=`root`@`localhost` PROCEDURE `update_author`(IN id int, IN newName varchar(45))
BEGIN
	IF newName != '' THEN
		UPDATE tbl_author a
        SET a.authorName = newName
        WHERE a.authorID = id;
	END IF;

END