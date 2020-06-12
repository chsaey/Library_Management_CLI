CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_book_copies`(IN book_id INT, IN branch_id INT, IN book_copies INT)
BEGIN
INSERT INTO tbl_book_copies (bookId, branchId, noOfCopies)
VALUES(book_id, branch_id, book_copies);
END