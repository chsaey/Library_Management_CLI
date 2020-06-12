CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_book_author`(IN bID int, IN aID int)
BEGIN
INSERT INTO tbl_book_authors (bookID, authorID)
VALUES(bID, aID);
END