import db_connections as dbc

def get_card_matches(cardNo):
    """Searches DB for the passed in card number. As tbl_borrower.cardNo is a
    is a PK there should be at most one value in the result set"""
    query = "SELECT tb.cardNo FROM tbl_borrower tb WHERE tb.cardNo=%s"
    libDB_cursor= dbc.get_db_cursor()
    libDB_cursor.execute(query, (cardNo,))#even a single param value needs to be in a tuple
    result = libDB_cursor.fetchone()
    #closing connection
    libDB_cursor.close()
    return result

def get_all_branches():
    """Simple query to get the information of all branches in DB"""
    query = "SELECT * FROM tbl_library_branch tbl"
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.execute(query)
    branch_list = []
    for branch in libDB_cursor:
        branch_list.append(branch)
    libDB_cursor.close()  
    return branch_list
    
def find_books_available_for_checkout(cardNo, branchId):
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.callproc('find_books_available_for_checkout', (cardNo, branchId))
    book_list=None
    for books in libDB_cursor.stored_results():#This loop loops only 1 because of stored_results
        book_list=books.fetchall()#fetchall returns a list of results 
    libDB_cursor.close()
    return book_list

def find_books_available_for_return(cardNo, branchId):
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.callproc('find_books_available_for_return', (cardNo, branchId))
    book_list=None
    for books in libDB_cursor.stored_results():#This loop loops only 1 because of stored_results
        book_list=books.fetchall()#fetchall returns a list of results 
    libDB_cursor.close()
    return book_list

def checkout_book(query_tuple):
    libDB_cursor = dbc.get_db_cursor()
    loan_info=libDB_cursor.callproc('checkout_book', query_tuple)
    dbc.commit_db()
    libDB_cursor.close()
    return loan_info

def return_book(query_tuple):
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.callproc('return_book', query_tuple)
    dbc.commit_db()
    libDB_cursor.close()
    