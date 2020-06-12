CREATE DEFINER=`root`@`localhost` PROCEDURE `find_books_available_for_checkout`(IN cur_cardNo INT, IN cur_branchId INT)
BEGIN
	SELECT DISTINCT tb.bookId, title, aut.authorName
    FROM tbl_book tb
    RIGHT JOIN tbl_book_copies tbc ON tb.bookId=tbc.bookId
    INNER JOIN tbl_library_branch tlb ON tbc.branchId=tlb.branchId
    INNER JOIN tbl_book_authors tba ON tb.bookId=tba.bookId
    INNER JOIN tbl_author aut ON tba.authorId=aut.authorId
    WHERE tbc.branchId=cur_branchId AND tbc.noOfCopies > (
		SELECT Count(*) FROM tbl_book_copies stock
        LEFT JOIN tbl_book_loans loans ON stock.bookId=loans.bookId
        WHERE tbc.bookId=stock.bookId AND stock.branchId=tbc.branchId AND  (loans.bookReturned IS NULL OR loans.bookReturned='n') 
	)AND tbc.bookId NOT IN (
		SELECT tbl.bookId FROM tbl_book_loans tbl
        WHERE tb.bookId=tbl.bookId AND tbl.branchId=cur_branchId AND tbl.cardNo=cur_cardNo AND bookReturned='n'
    );
END