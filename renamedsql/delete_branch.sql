CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_branch`(IN id int)
BEGIN
DELETE FROM tbl_library_Branch WHERE BranchID = id; 
END