CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_book`(IN id int)
BEGIN
DELETE FROM tbl_book WHERE bookID = id; 
END