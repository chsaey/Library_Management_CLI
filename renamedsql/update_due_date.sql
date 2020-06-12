CREATE DEFINER=`root`@`localhost` PROCEDURE `update_due_date`(in bookid INT, branchid Int, IN cardNo int, in days int)
BEGIN
UPDATE tbl_book_loans bl
SET bl.dueDate = date_add(dueDate, INTERVAL days day)
WHERE bl.bookid = bookid and bl.branchid = branchid and bl.cardNo = cardno;

END