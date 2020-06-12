CREATE DEFINER=`root`@`localhost` PROCEDURE `find_book_author`(IN bookId int, In authorId int)
BEGIN
Select exists(select * from tbl_book_authors ba Where ba.bookid = bookid and ba.authorid = authorid);

END