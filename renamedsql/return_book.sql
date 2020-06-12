CREATE DEFINER=`root`@`localhost` PROCEDURE `return_book`(IN user_cardno INT, IN checkout_branchId INT, IN checkout_bookId INT)
BEGIN
	UPDATE tbl_book_loans
    SET bookReturned='y'
    WHERE cardNo=user_cardno AND branchId=checkout_branchId AND bookId=checkout_bookId AND bookReturned='n';
END