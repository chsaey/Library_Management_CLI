CREATE DEFINER=`root`@`localhost` PROCEDURE `find_branches`()
BEGIN
Select *
From tbl_library_branch;
END