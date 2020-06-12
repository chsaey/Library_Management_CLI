CREATE DEFINER=`root`@`localhost` PROCEDURE `borrower_book_loans`(IN cardNo int)
BEGIN
	Select * from tbl_book_loans bl where bl.cardNo = cardNo and bl.bookReturned = 'n';
END