CREATE DEFINER=`root`@`localhost` PROCEDURE `display_authors_of_book`(IN bookid INT)
BEGIN
select authorName From tbl_author a
JOIN tbl_book_authors ba on ba.bookid
where ba.bookid = bookid and a.authorID = ba.authoriD;
END