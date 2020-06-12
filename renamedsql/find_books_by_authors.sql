CREATE DEFINER=`root`@`localhost` PROCEDURE `find_books_by_authors` ()
BEGIN
	SELECT DISTINCT tb.bookId, title, aut.authorName
    FROM tbl_book tb
    INNER JOIN tbl_book_authors tba ON tb.bookId=tba.bookId
    INNER JOIN tbl_author aut ON tba.authorId=aut.authorId;
END