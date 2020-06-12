CREATE DEFINER=`root`@`localhost` PROCEDURE `card_exists`(IN cardNo varchar(45), OUT e int)
BEGIN
Select exists(Select * from tbl_borrower b where b.cardNo = cardNo )
into e;
END