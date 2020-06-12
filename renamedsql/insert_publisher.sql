CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_publisher`(IN pubName varchar(45), IN address varchar(45), IN phoneNum varchar(45))
BEGIN
DECLARE newID int;
DECLARE newAddress varchar(45);
DECLARE newPhone varchar(45);
SET newAddress = NULL;
SET newPhone = NULL;
if address != '' THEN SET newAddress = address;
end if;
if phoneNum != '' THEN SET newPhone = phoneNum ;
end if;
SET newID = (select distinct max(publisherID) as maxVal FROM tbl_publisher) + 1;
INSERT INTO tbl_publisher (publisherID, publisherName, publisherAddress, publisherPhone)
VALUES(newID, pubName, newAddress, newPhone); 

END