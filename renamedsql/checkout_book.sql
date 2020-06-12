CREATE DEFINER=`root`@`localhost` PROCEDURE `checkout_book`(IN user_cardno INT, IN checkout_branchId INT, IN checkout_bookId INT, OUT due_date DATE)
BEGIN
	DECLARE checkout_date DATETIME;
    SET checkout_date = now();
    IF EXISTS (SELECT * FROM tbl_book_loans tbl WHERE tbl.cardNo=user_cardno AND tbl.bookId=checkout_bookId AND tbl.branchId=checkout_branchId AND tbl.bookReturned='y')
	THEN
        UPDATE tbl_book_loans tbl SET tbl.dateOut=checkout_date, tbl.dueDate=date_add(checkout_date,INTERVAL 7 DAY), tbl.bookReturned='n' 
        WHERE tbl.cardNo=user_cardno AND tbl.branchId=checkout_branchId AND tbl.bookId=checkout_bookId;
	ELSE
        INSERT INTO tbl_book_loans
        VALUES (checkout_bookId, checkout_branchId, user_cardno, checkout_date, date_add(checkout_date,INTERVAL 7 DAY), 'n');
        SELECT dueDate INTO due_date FROM tbl_book_loans tbl
        WHERE tbl.cardNo=user_cardno AND tbl.branchId=checkout_branchId AND tbl.bookId=checkout_bookId AND tbl.bookReturned='n';
    END IF; 
END