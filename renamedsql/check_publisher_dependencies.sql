CREATE DEFINER=`root`@`localhost` PROCEDURE `check_publisher_dependencies`(IN pub int, OUT n int)
BEGIN
SELECT count(*)
INTO n
FROM tbl_book b
WHERE b.pubId = pub;
END