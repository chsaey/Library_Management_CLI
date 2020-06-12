CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_book_author`(IN bookid int, IN authorid int)
BEGIN
IF authorID = -1 THEN
DELETE FROM tbl_book_authors ba WHERE ba.bookid = bookid; 
END IF;

IF bookid > 0 and authorid > 0 THEN
DELETE FROM tbl_book_authors ba WHERE ba.authorid = authorID and ba.bookid = bookid; 
END IF;
END