CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_branch`(IN brname varchar(45), IN addr varchar(45))
BEGIN
DECLARE newID int;
SET newID = (select distinct max(branchID) as maxVal FROM tbl_library_branch) + 1;
INSERT INTO tbl_library_branch (branchID, branchName, branchAddress)
VALUES(newID, brname, addr); 
END