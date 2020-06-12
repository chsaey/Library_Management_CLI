CREATE DEFINER=`root`@`localhost` PROCEDURE `find_author`(
IN name char(64),
OUT id int)
BEGIN
	Declare temp int Default 0;
	Select Distinct a.authorId
	Into temp  /* sets temp value to be authorId value */
	From tbl_author a
	Where a.authorName = name;
	Set id = temp;
END