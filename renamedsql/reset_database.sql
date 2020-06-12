CREATE DEFINER=`root`@`localhost` PROCEDURE `reset_database`()
BEGIN
SET FOREIGN_KEY_CHECKS=0;
truncate tbl_author;
truncate tbl_book;
truncate tbl_book_authors;
truncate tbl_book_copies;
truncate tbl_book_loans;
truncate tbl_borrower;
truncate tbl_library_branch;
truncate tbl_publisher;
SET FOREIGN_KEY_CHECKS=1;

-- add borrowers
INSERT INTO tbl_borrower(name, address, phone)
VALUES
	('John Cena', 'Cena Avenue', '123-456-7890'),
	('Mike Hawke', '123 Elm Street', '432-543-6743'),
	('John Doe', '1 Temp Street', '911');
-- add authors
INSERT INTO tbl_author(authorName)
VALUES
	('John Cena'),
    ('J.R.R. Tolkien'),
    ('J.K. Rowling'),
    ('C.S. Lewis');
-- add publishers
INSERT INTO tbl_publisher(publisherName, publisherAddress, publisherPhone)
VALUES
	('Cena inc', '123 Cena street', '432-432-4321'),
    ('Allen & Unwin', 'Australia', '654-654-6543'),
    ('Bloomsburg Publishing', 'London, United Kingdom', '876-876-8765'),
    ('Geoffrey Bles', 'London, United Kingdom', '234-456-6789');
-- add branches
INSERT INTO tbl_library_branch(branchName, branchAddress)
VALUES 
	('University Library', 'Boston'),
    ('State Library', 'Boston'),
    ('Federal Library', 'Washington DC'),
    ('County Library', 'McLean VA');
-- add books
INSERT INTO tbl_book(title, pubId)
VALUES 
	('The Lord of the Rings: The Fellowship of the Ring', (Select publisherId From tbl_publisher where publisherName = 'Allen & Unwin')),
    ('Harry Potter and the Sorcerer"s Stone', (Select publisherId From tbl_publisher where publisherName = 'Bloomsburg Publishing')),
    ('The Chronicles of Narnia: The Magician"s Nephew', (Select publisherId From tbl_publisher where publisherName = 'Geoffrey Bles'));
-- add author-book pairs
INSERT IGNORE INTO tbl_book_authors(bookId, authorId)
VALUES
	((Select bookId From tbl_book Where title = 'The Lord of the Rings: The Fellowship of the Ring'),
	(Select authorId From tbl_author Where authorName = 'J.R.R. Tolkien')),
	((Select bookId From tbl_book Where title = 'Harry Potter and the Sorcerer"s Stone'),
	(Select authorId From tbl_author Where authorName = 'J.K. Rowling')),
	((Select bookId From tbl_book Where title = 'The Chronicles of Narnia: The Magician"s Nephew'),
	(Select authorId From tbl_author Where authorName = 'C.S. Lewis'));
-- add book copies
INSERT IGNORE INTO tbl_book_copies(bookId, branchId, noOfCopies)
VALUES
	((Select bookId From tbl_book Where title = 'The Lord of the Rings: The Fellowship of the Ring'),
    (Select BranchId From tbl_library_branch Where branchName = 'University Library'),
    5),
    ((Select bookId From tbl_book Where title = 'Harry Potter and the Sorcerer"s Stone'),
	(Select BranchId From tbl_library_branch Where branchName = 'State Library'),
    10),
	((Select bookId From tbl_book Where title = 'The Chronicles of Narnia: The Magician"s Nephew'),
    (Select BranchId From tbl_library_branch Where branchName = 'Federal Library'),
    15),
	((Select bookId From tbl_book Where title = 'The Lord of the Rings: The Fellowship of the Ring'),
    (Select BranchId From tbl_library_branch Where branchName = 'Federal Library'),
    20);

END