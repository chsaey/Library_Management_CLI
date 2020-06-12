CREATE DEFINER=`root`@`localhost` PROCEDURE `update_book_copies`(IN cur_bookId int, IN cur_branchId int, IN cur_noOfCopies int)
BEGIN
		UPDATE tbl_book_copies tbc
        SET tbc.noOfCopies = cur_noOfCopies
        WHERE tbc.bookId = cur_bookId AND tbc.branchid = cur_branchId;
END