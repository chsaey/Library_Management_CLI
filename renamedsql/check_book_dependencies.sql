CREATE DEFINER=`root`@`localhost` PROCEDURE `check_book_dependencies`(IN book int, OUT n int)
BEGIN
SELECT count(*)
INTO n
FROM tbl_book_authors ba, tbl_book_loans l, tbl_book_copies c
WHERE ba.bookId = book and l.bookId = book and c.bookId = book;
END