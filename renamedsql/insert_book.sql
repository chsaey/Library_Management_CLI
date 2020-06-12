CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_book`(IN title varchar(45), IN publisher int)
BEGIN
DECLARE newID int;
SET newID = (select distinct max(bookId) as maxVal FROM tbl_book) + 1;
if publisher = 0 THEN
INSERT INTO tbl_book (bookId, title, pubId)
VALUES(newID, title, NULL);
ELSE 
INSERT INTO tbl_book (bookId, title, pubId)
VALUES(newID, title, publisher); 

end if;
END