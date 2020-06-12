CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_author`(IN authName varchar(45))
BEGIN
DECLARE newID int;
SET newID = (select distinct max(authorId) as maxVal FROM tbl_author) + 1;
INSERT INTO tbl_author (authorID, authorName)
VALUES(newID, authName); 
END