CREATE DEFINER=`root`@`localhost` PROCEDURE `display_book_copies`(IN cur_bookId INT, 
IN cur_branchId INT )
    READS SQL DATA
BEGIN
	 SELECT noOfCopies 
FROM tbl_book_copies tbc
WHERE tbc.bookId = cur_bookId AND tbc.branchid = cur_branchId;
END
