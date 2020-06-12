CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_author`(IN id int)
BEGIN
DELETE FROM tbl_Author WHERE authorID = id; 
END