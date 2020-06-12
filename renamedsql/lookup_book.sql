CREATE DEFINER=`root`@`localhost` PROCEDURE `lookup_book`(
IN title char(64),
OUT id int)
BEGIN 
	Declare temp int Default 0;
	Select Distinct b.bookId
	Into temp  /* sets temp value to be bookId value */
		From tbl_book b
		Where b.title = title; 
		Set id = temp;
END