CREATE DEFINER=`root`@`localhost` PROCEDURE `check_borrower_dependencies`(IN card int, OUT n int)
BEGIN
SELECT count(*)
INTO n
FROM tbl_book_loans l
WHERE l.cardNo = card AND l.bookReturned='n';
END