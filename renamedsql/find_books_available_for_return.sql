CREATE DEFINER=`root`@`localhost` PROCEDURE `find_books_available_for_return`(IN cur_cardNo INT, IN cur_branchId INT)
BEGIN
	SELECT tb.bookId, tb.title, aut.authorName
    FROM tbl_book tb
    INNER JOIN tbl_book_authors tba ON tb.bookId=tba.bookId
    INNER JOIN tbl_author aut ON tba.authorId=aut.authorId
    INNER JOIN tbl_book_loans tbl ON tb.bookId=tbl.bookId
    WHERE tbl.branchId=cur_branchId AND tbl.cardNo=cur_cardNo AND tbl.bookReturned='n';
END