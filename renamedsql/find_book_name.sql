CREATE DEFINER=`root`@`localhost` PROCEDURE `find_book_name`(IN bookid INT, out bkname varchar(45))
BEGIN
select b.title from tbl_book b where b.bookid = bookid
into bkname;

END