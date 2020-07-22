import db_connections as dbc
import mysql

def reset_database():
    cursor = dbc.get_db_cursor()  
    cursor.callproc('reset_database')

def proc(proc, args):
    cursor = dbc.get_db_cursor()  
    cursor.callproc(proc, args)  
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
    try:
        cursor.callproc('insert_book_author', args)
        dbc.commit_db()
    except mysql.connector.IntegrityError as err:
        print('This author is already associated with this book!')

def insert_book_copies(bookId, branchId, noOfCopies):
    cursor = dbc.get_db_cursor()  
    args = (bookId, branchId, noOfCopies)
    cursor.callproc('insert_book_copies', args)
    dbc.commit_db()

def lookup(proc, info):
    cursor = dbc.get_db_cursor()
    results = cursor.callproc(proc, info) 
    return results[1]

def check(proc, args):
    cursor = dbc.get_db_cursor()
    results = cursor.callproc(proc, args)   
    return results[1]

def lookup_due_date(cardNo, bookId, branchId):
    cursor = dbc.get_db_cursor()   
    args = [cardNo, bookId, branchId]
    result = cursor.callproc('lookup_due_date', args)
    return result[0]

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

def lookup_book_author(bookID, authorID):
    cursor = dbc.get_db_cursor() 
    args = (bookID, authorID)
    cursor.callproc('find_book_author', args)
    for result in cursor.stored_results():
        book_authors = result.fetchall()
    return book_authors[0][0]

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
        print('Name:', book[1])
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
