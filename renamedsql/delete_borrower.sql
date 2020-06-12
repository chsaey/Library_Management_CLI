CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_borrower`(IN card int)
BEGIN
IF NOT EXISTS(
  SELECT * 
  FROM tbl_book_loans l
  WHERE l.cardNo = card
)
THEN
DELETE FROM tbl_borrower WHERE cardNo = card; 
END IF;

END