CREATE DEFINER=`root`@`localhost` PROCEDURE `find_borrower`(
IN name char(64),
OUT id int)
BEGIN
	Declare temp int Default 0;
	Select Distinct b.cardno
	Into temp  /* sets temp value to be borrowerCardNo value */
	From tbl_borrower b
	Where b.name = name;
	Set id = temp;
END