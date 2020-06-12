CREATE DEFINER=`root`@`localhost` PROCEDURE `display_branches`()
    READS SQL DATA
BEGIN
	select * From tbl_library_branch;
END