CREATE DEFINER=`root`@`localhost` PROCEDURE `check_author_dependencies`(IN author int, OUT n int)
BEGIN
SELECT count(*)
INTO n
FROM tbl_book_authors ba
WHERE ba.authorId = author;
END