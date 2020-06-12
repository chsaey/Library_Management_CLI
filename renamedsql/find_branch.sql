CREATE DEFINER=`root`@`localhost` PROCEDURE `find_branch`(
IN lbname char(64),
OUT id int)
BEGIN
	Declare temp int Default 0;
	Select Distinct lb.branchID
	Into temp  /* sets temp value to be authorId value */
	From tbl_library_branch lb
	Where lb.branchName = lbname;
	Set id = temp;
END