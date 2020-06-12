CREATE DEFINER=`root`@`localhost` PROCEDURE `display_books`()
    READS SQL DATA
BEGIN
	select * From tbl_book;
END
