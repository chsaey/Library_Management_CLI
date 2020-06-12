CREATE DEFINER=`root`@`localhost` PROCEDURE `lookup_due_date`(In cardNo int, In bookId int, In  branchId int, out d Datetime)
BEGIN
Select dueDate
Into d
From tbl_book_loans l
Where l.cardNo = cardNo and l.bookId = bookId and l.branchId = branchId and l.bookReturned = 'N';
END