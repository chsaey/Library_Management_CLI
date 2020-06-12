CREATE DEFINER=`root`@`localhost` PROCEDURE `update_branch`(IN brid int, IN newName varchar(45), IN newAddr varchar(45))
BEGIN
	IF newName != '' THEN
		UPDATE tbl_library_branch lb
        SET lb.branchName = newName
        WHERE lb.branchid = brid;
	END IF;
	IF newAddr != '' THEN
		UPDATE tbl_library_branch lb
        SET lb.branchAddress = newAddr
        WHERE lb.branchid = brid;
	END IF;
END