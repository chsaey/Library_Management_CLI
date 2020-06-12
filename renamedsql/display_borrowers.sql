CREATE DEFINER=`root`@`localhost` PROCEDURE `display_borrowers`()
    READS SQL DATA
BEGIN
	select * From tbl_borrower;
END