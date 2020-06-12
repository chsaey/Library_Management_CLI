CREATE DEFINER=`root`@`localhost` PROCEDURE `check_branch_dependencies`(IN branch int, OUT n int)
BEGIN
SELECT count(*)
INTO n
FROM tbl_book_copies c, tbl_book_loans l
WHERE c.branchId = branch and l.branchId = branch;
END