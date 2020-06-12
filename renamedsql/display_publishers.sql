CREATE DEFINER=`root`@`localhost` PROCEDURE `display_publishers`()
    READS SQL DATA
BEGIN
	select * From tbl_publisher;
END
