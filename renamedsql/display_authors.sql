CREATE DEFINER=`root`@`localhost` PROCEDURE `display_authors`()
    READS SQL DATA
BEGIN
	select * From tbl_author;
END