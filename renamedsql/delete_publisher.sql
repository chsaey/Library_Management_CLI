CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_publisher`(IN id int)
BEGIN
DELETE FROM tbl_publisher WHERE publisherID = id; 
END