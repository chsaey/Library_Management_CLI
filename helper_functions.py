import db_connections as dbc

def lookup_due_date(cardNo, bookId, branchId):
    cursor = dbc.get_db_cursor()   
    args = [cardNo, bookId, branchId]
    result = cursor.callproc('lookup_due_date', args)
    return result[0]

def reset_database():
    cursor = dbc.get_db_cursor()  
    cursor.callproc('reset_database')

def insert_book(title, pubId):
    args = (title, int(pubId))
    cursor = dbc.get_db_cursor()  
    cursor.callproc('insert_book', args)  
    dbc.commit_db()

def insert_publisher(name, address, phone):
    args = (name, address, phone)
    cursor = dbc.get_db_cursor()  
    cursor.callproc('insert_publisher', args)
    dbc.commit_db()

def insert_author(name): 
    args = (name,) 
    cursor = dbc.get_db_cursor()      
    cursor.callproc('insert_author', args)
    dbc.commit_db()

def insert_branch(name, address):
    args = (name, address)
    cursor = dbc.get_db_cursor()  
    cursor.callproc('insert_branch', args)
    dbc.commit_db()

def insert_borrower(name, address, phone):
    cursor = dbc.get_db_cursor()  
    args = (name, address, phone, 0)
    results = cursor.callproc('insert_borrower', args)   
    dbc.commit_db()
    return results[3]

def insert_book_author(bookID, authorID):
    cursor = dbc.get_db_cursor()  
    args = (bookID, authorID)
    cursor.callproc('insert_book_author', args)
    dbc.commit_db()

def insert_book_copies(bookId, branchId, noOfCopies):
    cursor = dbc.get_db_cursor()  
    args = (bookId, branchId, noOfCopies)
    cursor.callproc('insert_book_copies', args)
    dbc.commit_db()

def lookup_branch(branch):    
    return lookup_results('find_branch', branch)
    
def lookup_book(title): 
    return lookup_results('find_book', title)  

def lookup_borrower(card):
    return lookup_results('find_borrower', card)  

def lookup_author(author):
    return lookup_results('find_author', author)   

def lookup_publisher(publisher):    
    return lookup_results('find_publisher', publisher)

def lookup_results(proc, info):
    cursor = dbc.get_db_cursor()
    results = cursor.callproc(proc, [info, 0]) 
    return results[1]

def lookup_authors_of_book(bookid):
    cursor = dbc.get_db_cursor() 
    args = (bookid,)
    cursor.callproc('display_authors_of_book', args)
    for result in cursor.stored_results():
        book_Authors = result.fetchall()
    count = 1
    for authors in book_Authors:
        print(str(count)+'.', authors[0])
        count+=1
    return book_Authors

def lookup_book_author(bookID,authorID):
    cursor = dbc.get_db_cursor() 
    args = (bookID, authorID)
    cursor.callproc('find_book_author', args)
    for result in cursor.stored_results():
        book_authors = result.fetchall()
    return book_authors[0][0]

def edit_branch(branchID, name, address):
    cursor = dbc.get_db_cursor() 
    args = (branchID, name, address)
    cursor.callproc('update_branch', args)
    dbc.commit_db()

def edit_book_copies(bookId, branchId, noOfCopies):
  cursor = dbc.get_db_cursor()
  args = (bookId, branchId, noOfCopies)
  cursor.callproc('update_book_copies', args)
  dbc.commit_db()

def edit_author(authorID, name):
    cursor = dbc.get_db_cursor()
    args = (authorID, name)
    cursor.callproc('update_author', args)
    dbc.commit_db()

def edit_book(bookID, name, address):
    cursor = dbc.get_db_cursor()
    args = (bookID, name, address)
    cursor.callproc('update_book', args)
    dbc.commit_db()

def edit_borrower(card, name, address, phone):
    cursor = dbc.get_db_cursor()
    args = (card, name, address, phone)
    cursor.callproc('update_borrower', args)
    dbc.commit_db()

def edit_publisher(publisherID, name, address, phone):
    cursor = dbc.get_db_cursor()
    args = (publisherID, name, address, phone)
    cursor.callproc('update_publisher', args)
    dbc.commit_db()

def remove_author(authorid):
    cursor = dbc.get_db_cursor()
    args = (authorid,)
    cursor.callproc('delete_author', args)
    dbc.commit_db()

def remove_book(bookid):
    cursor = dbc.get_db_cursor()
    args = (bookid,)
    cursor.callproc('delete_book', args)
    dbc.commit_db()

def remove_borrower(borrowerid):
    cursor = dbc.get_db_cursor()
    args = (borrowerid,)
    cursor.callproc('delete_borrower', args)
    dbc.commit_db()

def remove_branch(branchid):
    cursor = dbc.get_db_cursor()
    args = (branchid,)
    cursor.callproc('delete_branch', args)
    dbc.commit_db()

def remove_publisher(publisherid):
    cursor = dbc.get_db_cursor()
    args = (publisherid,)
    cursor.callproc('delete_publisher', args)
    dbc.commit_db()

def remove_book_author(bookid,adminid):
    cursor = dbc.get_db_cursor()
    args = (bookid, adminid)
    cursor.callproc('delete_book_author', args)
    dbc.commit_db()

def display_branches():
    cursor = dbc.get_db_cursor()
    cursor.callproc('display_branches')    
    for result in cursor.stored_results():
        branches=result.fetchall()
    count = 1
    for branch in branches:  
        print(count, end=') ')      
        print('Name:',branch[1], end=' ')
        print('Address:',branch[2])
        count+=1
    return branches

def display_borrowers():
    cursor = dbc.get_db_cursor()
    cursor.callproc('display_borrowers')    
    for result in cursor.stored_results():
        borrowers=result.fetchall()
    count = 1
  
    for borrower in borrowers:  
        print(count, end=') ')      
        print('CardNum:',borrower[0], end=' ')      
        print('Name:',borrower[1], end=' ')
        print('Address:',borrower[2], end=' ')
        print('Phone:',borrower[3])
        count+=1
    return borrowers

def display_books():
    cursor = dbc.get_db_cursor()
    cursor.callproc('display_books')    
    for result in cursor.stored_results():
        books=result.fetchall()
    count = 1
    for book in books:  
        print(count, end=') ')      
        print('Name:',book[1])
        count+=1
    return books

def display_publishers():
    cursor = dbc.get_db_cursor()
    cursor.callproc('display_publishers')    
    for result in cursor.stored_results():
        publishers=result.fetchall()
    count = 1
    for publisher in publishers:  
        print(count, end=') ')      
        print('Name:', publisher[1])        
        count+=1
    return publishers

def display_authors():
    cursor = dbc.get_db_cursor()
    cursor.callproc('display_authors')    
    for result in cursor.stored_results():
        authors=result.fetchall()
    count = 1
    for author in authors:  
        print(count, end=') ')      
        print('Name:', author[1])        
        count+=1
    return authors

def check_publisher_dependencies(publisherID):
    cursor = dbc.get_db_cursor()
    args = (publisherID, 0)
    results = cursor.callproc('check_publisher_dependencies', args)   
    return results[1]

def check_branch_dependencies(BranchID):
    cursor = dbc.get_db_cursor()
    args = (BranchID, 0)
    results = cursor.callproc('check_branch_dependencies', args)   
    return results[1]

def check_book_dependencies(bookID):
    cursor = dbc.get_db_cursor()
    args = (bookID, 0)
    results = cursor.callproc('check_book_dependencies', args)   
    return results[1]

def check_author_dependencies(authorID):
    cursor = dbc.get_db_cursor()
    args = (authorID, 0)
    results = cursor.callproc('check_author_dependencies', args)   
    return results[1]
def check_borrower_dependencies(cardNo):
    cursor = dbc.get_db_cursor()
    args = (cardNo, 0)
    results = cursor.callproc('check_borrower_dependencies', args)   
    return results[1]

def display_borrower_books(cardNo):
    cursor = dbc.get_db_cursor()
    args = (cardNo,)
    result = cursor.callproc('borrower_book_loans', args)
    for result in cursor.stored_results():
        book_loans=result.fetchall()
    count = 1
    for book_loan in book_loans:   
       
        bkname = cursor.callproc('find_book_name', (book_loan[0], 0))    
        print(count, end=') ')    
        print(str(bkname[1]), 'DueDate: ', book_loan[4])    
        count+=1

    return book_loans

def edit_due_date(bookid, branchid, cardno, days):
    cursor = dbc.get_db_cursor()
    args = (bookid, branchid, cardno, days)    
    cursor.callproc('update_due_date', args)
    dbc.commit_db()

def card_exists(cardNo):
    cursor = dbc.get_db_cursor()
    args = (cardNo, 0 )
    results = cursor.callproc('card_exists', args)
    return results[1]




