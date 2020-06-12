import db_connections as dbc

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

def get_all_books():
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.callproc('find_books_by_authors')
    book_list=None
    for books in libDB_cursor.stored_results():#This loop loops only 1 because of stored_results
        book_list=books.fetchall()#fetchall returns a list of results 
    libDB_cursor.close()
    return book_list

def get_noOfCopies(bookId, branchId):
    libDB_cursor= dbc.get_db_cursor()
    libDB_cursor.callproc('display_book_copies', (bookId, branchId))
    for books in libDB_cursor.stored_results():#This loop loops only 1 because of stored_results
        book_copies=books.fetchone()
    # book_copies = libDB_cursor.execute(query, (bookId, branchId))#even a single param value needs to be in a tuple
    libDB_cursor.close()
    return book_copies

def edit_branch(branchId, branchName, branchAddress):
    libDB_cursor = dbc.get_db_cursor()
    libDB_cursor.callproc('update_branch', (branchId, branchName, branchAddress))
    dbc.commit_db()
    libDB_cursor.close()
