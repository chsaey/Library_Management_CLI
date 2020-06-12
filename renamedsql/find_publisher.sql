CREATE DEFINER=`root`@`localhost` PROCEDURE `find_publisher`(
IN name char(64),
OUT id int)
BEGIN
	Declare temp int Default 0;
	Select Distinct p.publisherId
	Into temp /* sets temp value to be publisherId value */
	From tbl_publisher p
	Where p.publisherName = name;
	Set id = temp;
END